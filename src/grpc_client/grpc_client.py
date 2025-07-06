import grpc

from proto_gen import sensors_pb2_grpc, sensors_pb2
from google.protobuf.empty_pb2 import Empty
from dataclasses import dataclass

@dataclass
class ImuData:
    timestamp: int
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    angular_velocity_x: float
    angular_velocity_y: float
    angular_velocity_z: float

class GrpcImuClient:
    def __init__(self, server_address='host.docker.internal:50051'):
        self.server_address = server_address
        self.channel = grpc.insecure_channel(self.server_address)
        self.stub = sensors_pb2_grpc.SensorServiceStub(self.channel)

    def GetImu(self) -> ImuData | None:
        try:
            request = Empty()
            imu_stream = self.stub.getImu(request)
            imu:sensors_pb2.IMUData = next(imu_stream, None)
            
            return ImuData(
                timestamp=imu.timestamp,
                acceleration_x=imu.ax,
                acceleration_y=imu.ay,
                acceleration_z=imu.az,
                angular_velocity_x=imu.gx,
                angular_velocity_y=imu.gy,
                angular_velocity_z=imu.gz
            )
        except Exception as e:
            print(f"Error: {e}")
            return None

    def close(self):
        self.channel.close()

# For testing purposes, you can run this script directly to get a sample IMU data.
if __name__ == "__main__":
    client = GrpcImuClient()
    imu = client.GetImu()
    if imu is not None:
        print(f"IMU Data: {imu}")
    client.close()