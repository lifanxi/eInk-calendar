import asyncio
from bleak import BleakScanner

async def scan_for_devices(timeout=10):
    """扫描蓝牙设备并返回 MAC 地址和本地名称"""
    devices = await BleakScanner.discover(timeout=timeout)
    results = []
    for device in devices:
        # 获取设备的 MAC 地址和本地名称（广告中的名称）
        mac_address = device.address
        local_name = device.name if device.name else "Unknown"
        results.append({
            "MAC Address": mac_address,
            "Local Name": local_name
        })
    return results

async def main():
    print("开始扫描蓝牙设备（5秒）...")
    devices = await scan_for_devices()
    if not devices:
        print("未发现任何蓝牙设备！")
        return
    
    print("\n发现的设备列表：")
    for idx, dev in enumerate(devices, 1):
        print(f"设备 {idx}:")
        print(f"  MAC 地址: {dev['MAC Address']}")
        print(f"  设备名称: {dev['Local Name']}\n")

if __name__ == "__main__":
    asyncio.run(main())
