import asyncio
from bleak import BleakClient, BleakScanner
from datetime import datetime

# ESP32 的 MAC 地址（需替换为实际地址）
ESP32_MAC_ADDRESS = "3C:8A:1F:77:50:2E"
SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

async def connect_and_send_data(address):
    device = await BleakScanner.find_device_by_address(address)
    if not device:
        print("未找到 ESP32 设备！")
        return

    async with BleakClient(device) as client:
        print(f"Connected to {address}")
        
        # 发送数据到 ESP32（示例：发送 "Hello from PC"）
        await client.write_gatt_char(CHARACTERISTIC_UUID, f"""{{"datetime":"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"}}""".encode("ascii"))
        print("数据已发送！")

        await asyncio.sleep(2)
        await client.disconnect()

if __name__ == "__main__":
    while True:
        asyncio.run(connect_and_send_data(ESP32_MAC_ADDRESS))
