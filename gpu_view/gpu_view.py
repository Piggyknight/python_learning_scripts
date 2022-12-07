import os
import time
import threading
import atexit

class Enviroment:
    def __init__(self):
        self.env_map = {} 

    def process(self, value):
        cur = 0
        result = []

        while True:
            start = value.find("%", cur)
            if start < 0:
                break
            result.append(value[cur:start])
            end = value.find("%", start + 1)
            key = value[start + 1:end]
            result.append(self.get(key))
            cur = end + 1

        result.append(value[cur:])

        return "".join(result)

    def eval(self, cmd):
        eq = cmd.find("=")
        if (eq < 0):
            return
        self.set(cmd[:eq], cmd[eq+1:])

    def set(self, name, value):
        self.env_map[name] = self.process(value)

    def get(self, name):
        return self.env_map.get(name, "")

    def dump(self):
        print(self.env_map)

class Profiler:
    def __init__(self, xperf_path):
        self.xperf_path = xperf_path

        env = Enviroment()
        env.eval("TRACE_MIRAGE=356E1338-04AD-420E-8B8A-A2EB678541CF:0xf00000:5")
        env.eval("TRACE_DHD=19d9d739-da0a-41a0-b97f-24ed27abc9fb:0xffffff:5")
        env.eval("TRACE_DXVA2=a0386e75-f70c-464c-a9ce-33c44e091623:0xffff:5")
        env.eval("TRACE_MMCSS=f8f10121-b617-4a56-868b-9df1b27fe32c:0xffff:5")
        env.eval("TRACE_WMDRM=6e03dd26-581b-4ec5-8f22-601a4de5f022:0xffff:5")
        env.eval("TRACE_WME=8f2048e0-f260-4f57-a8d1-932376291682")
        env.eval("TRACE_WMP=681069c4-b785-466a-bc63-4aa616644b68:0xffff:5")
        env.eval("TRACE_DVD=75d4a1bb-7cc6-44b1-906d-d5e05be6d060:0xffff:5")
        env.eval("TRACE_DSHOW=28cf047a-2437-4b24-b653-b9446a419a69")
        env.eval("TRACE_MF=f404b94e-27e0-4384-bfe8-1d8d390b0aa3+362007f7-6e50-4044-9082-dfa078c63a73:0x000000000000ffff:0x5")
        env.eval("TRACE_AE=a6a00efd-21f2-4a99-807e-9b3bf1d90285:0x000000000000ffff:0x5")
        env.eval("TRACE_HME=63770680-05F1-47E0-928A-9ACFDCF52147:0xffff:5")
        env.eval("TRACE_HDDVD=779d8cdc-666b-4bf4-a367-9df89d6901e8:0xffff:5")
        env.eval("TRACE_DWMAPIGUID=71dd85bc-d474-4974-b0f6-93ffc5bfbd04::6")
        env.eval("TRACE_SCHEDULEGUID=8cc44e31-7f28-4f45-9938-4810ff517464:0xffff:6")
        env.eval("TRACE_DX=DX")
        env.eval("TRACE_WARP=ee685ec4-8270-4b08-9e4e-8b356f48f92f:0")
        env.eval("TRACE_DXGI=CA11C036-0102-4A2D-A6AD-F03CFED5D3C9:0xf:6:'stack'")
        env.eval("TRACE_DXGIDEBUG=F1FF64EF-FAF3-5699-8E51-F6EC2FBD97D1:0xffffffffffffffff")
        env.eval("TRACE_DXGIDEBUG_LIGHT=%TRACE_DXGIDEBUG%:4")
        env.eval("TRACE_DXGIDEBUG_NORMAL=%TRACE_DXGIDEBUG%:4:'stack'")
        env.eval("TRACE_DXGIDEBUG_VERBOSE=%TRACE_DXGIDEBUG%:6:'stack'")
        env.eval("TRACE_DXGI_TELEMETRY=03bbe5b8-c788-4d0b-b47e-5b5731398a89")
        env.eval("TRACE_DXCORE=ab604427-d048-4139-8494-1246c81f09d5:0xffffffffffffffff:6:'stack'")
        env.eval("TRACE_D3D11ON12=a0ab5aac-e0a4-4f10-83c6-31939c604fd9:0xffffffffffffffff:6:'stack'")
        env.eval("TRACE_D3D9ON12=c0c418c5-1f3c-4ee0-93a2-a0bb8f417f9a:0xffffffffffffffff:6:'stack'")
        env.eval("TRACE_D3D12=5d8087dd-3a9b-4f56-90df-49196cdc4f11:0xffffffffffffffff:6:'stack'")
        env.eval("TRACE_D3D11=db6f6ddb-ac77-4e88-8253-819df9bbf140:0xffffffffffffffff:6:'stack'")
        env.eval("TRACE_D3D10LEVEL9=7E7D3382-023C-43cb-95D2-6F0CA6D70381:0x1")
        env.eval("TRACE_D3DSCACHE=2d4ebca6-ea64-453f-a292-ae2ea0ee513b:0xf:5")
        env.eval("TRACE_DXC=802ec45a-1e99-4b83-9920-87c98277ba9d")
        env.eval("TRACE_DXC_ALL=%TRACE_DXC%:0x90FFFF:5:'stack'")
        env.eval("TRACE_DXC_LONGHAUL=%TRACE_DXC%:0x800:5")
        env.eval("TRACE_DXC_MIN=%TRACE_DXC%:0x800:5")
        env.eval("TRACE_DXC_LIGHT=%TRACE_DXC%:0x826:5")
        env.eval("TRACE_DXC_NORMAL=%TRACE_DXC%:0x900236:5")
        env.eval("TRACE_DXC_STACKS=%TRACE_DXC%:0x208041:5:'stack'")
        env.eval("TRACE_UMD=a688ee40-d8d9-4736-b6f9-6b74935ba3b1:0xffff:5")
        env.eval("TRACE_DWM=a42c77db-874f-422e-9b44-6d89fe2bd3e5:0x000000007fffffff:0x5")
        env.eval("TRACE_DWM2=8c9dd1ad-e6e5-4b07-b455-684a9d879900:0xFFFF:6")
        env.eval("TRACE_DWM3=9e9bba3c-2e38-40cb-99f4-9e8281425164:0xFFFF:6")
        env.eval("TRACE_CODEC=ea6d6e3b-7014-4ab1-85db-4a50cda32a82:0xffff:5")
        env.eval("TRACE_KMFD=E7C7EDF9-D0E4-4338-8AE3-BCA3C5B4B4A3")
        env.eval("TRACE_UMFD=a70bc228-e778-4061-86fa-debb03fda64a")
        env.eval("TRACE_WDLOG=70e74dd8-39db-5f6f-6fd1-f5581b29e834")
        env.eval("TRACE_WDLOG_ALL=%TRACE_WDLOG%:0xffff:5")
        env.eval("TRACE_WDLOG_ERRORS=%TRACE_WDLOG%:0x3:5")
        env.eval("TRACE_TESTFRAMEWORK=31293f4f-f7bb-487d-8b3b-f537b827352f")
        env.eval("TRACE_TEST=42C4E0C1-0D92-46f0-842C-1E791FA78D52")
        env.eval("TRACE_SC=30336ed4-e327-447c-9de0-51b652c86108")
        env.eval("TRACE_XAML=531A35AB-63CE-4BCF-AA98-F88C7A89E455:0xffff")
        env.eval("TRACE_WIN32K=8c416c79-d49b-4f01-a467-e56d3aa8234c:0xffff")
        env.eval("TRACE_D2D=dcb453db-c652-48be-a0f8-a64459d5162e:0:5")
        env.eval("TRACE_D2DSCENARIOS=712909c0-6e57-4121-b639-87c8bf9004e0")
        env.eval("TRACE_D3D9_PRESENT=783ACA0A-790E-4d7f-8451-AA850511C6B9:0xf:6")
        env.eval("TRACE_DXGI_PRESENT=CA11C036-0102-4A2D-A6AD-F03CFED5D3C9:0xf:6")
        env.eval("TRACE_D3D11_PRESENT=db6f6ddb-ac77-4e88-8253-819df9bbf140:0xffffffffffffffff:6")
        env.eval("TRACE_DXC_ALL_PRESENT=%TRACE_DXC%:0x10FFFF:5")
        env.eval("TRACE_DXC_PRESENT=%TRACE_DXC%:0x208041:5")

        env.eval("TRACE_CS_PROVIDERS_MIN=%TRACE_UMD%+%TRACE_DXGI%+%TRACE_D3D11ON12%+%TRACE_D3D9ON12%+%TRACE_D3D12%+%TRACE_D3D11%+%TRACE_D3D10LEVEL9%")
        env.eval("TRACE_CS_PROVIDERS_PRESENT=%TRACE_UMD%+%TRACE_DXGI_PRESENT%+%TRACE_D3D11_PRESENT%+%TRACE_D3D9_PRESENT%+%TRACE_MIRAGE%+%TRACE_DHD%")
        env.eval("TRACE_CS_PROVIDERS_LIGHT=%TRACE_CS_PROVIDERS_MIN%+%TRACE_D3DSCACHE%")
        env.eval("TRACE_CS_PROVIDERS_NORMAL=%TRACE_CS_PROVIDERS_LIGHT%+%TRACE_MIRAGE%+%TRACE_DHD%")
        env.eval("TRACE_CS_PROVIDERS_VERBOSE=%TRACE_CS_PROVIDERS_NORMAL%")
        env.eval("TRACE_CS_STATE_MIN=%TRACE_UMD%+%TRACE_DXGI%+%TRACE_D3D11ON12%+%TRACE_D3D9ON12%+%TRACE_D3D12%+%TRACE_D3D11%+%TRACE_D3D10LEVEL9%")
        env.eval("TRACE_CS_STATE_PRESENT=%TRACE_UMD%+%TRACE_DXGI_PRESENT%+%TRACE_D3D11_PRESENT%+%TRACE_D3D9_PRESENT%")
        env.eval("TRACE_CS_STATE_LIGHT=%TRACE_CS_STATE_MIN%+%TRACE_D3DSCACHE%")
        env.eval("TRACE_CS_STATE_NORMAL=%TRACE_CS_STATE_LIGHT%")
        env.eval("TRACE_CS_STATE_VERBOSE=%TRACE_CS_STATE_NORMAL%")
        env.eval("SCHEDULER_LOG_STATE=%TRACE_DXC%:0x04000000:")
        env.eval("TRACE_NOCS_PROVIDERS_PRESENT=%TRACE_DXC_PRESENT%+%TRACE_DWM3%+%TRACE_WIN32K%")
        env.eval("TRACE_NOCS_PROVIDERS_MIN=%TRACE_DXC_STACKS%")
        env.eval("TRACE_NOCS_PROVIDERS_LIGHT_NODXGIDEBUG=%TRACE_NOCS_PROVIDERS_MIN%+%TRACE_MF%+%TRACE_WME%")
        env.eval("TRACE_NOCS_PROVIDERS_NORMAL_NODXGIDEBUG=%TRACE_NOCS_PROVIDERS_LIGHT_NODXGIDEBUG%+%TRACE_SCHEDULEGUID%+%TRACE_SC%+%TRACE_WIN32K%+%TRACE_DWM%+%TRACE_DWM2%+%TRACE_DWM3%+%TRACE_TESTFRAMEWORK%+%TRACE_TEST%+%TRACE_DSHOW%+%TRACE_AE%+%TRACE_DXVA2%+%TRACE_DXCORE%")
        env.eval("TRACE_NOCS_PROVIDERS_VERBOSE_NODXGIDEBUG=%TRACE_NOCS_PROVIDERS_NORMAL_NODXGIDEBUG%+%TRACE_D2DSCENARIOS%+%TRACE_D2D%+%TRACE_MMCSS%+%TRACE_WMDRM%+%TRACE_WMP%+%TRACE_DVD%+%TRACE_HME%+%TRACE_HDDVD%+%TRACE_DWMAPIGUID%+%TRACE_CODEC%")
        env.eval("TRACE_NOCS_PROVIDERS_LIGHT=%TRACE_NOCS_PROVIDERS_LIGHT_NODXGIDEBUG%+%TRACE_DXGIDEBUG_LIGHT%")
        env.eval("TRACE_NOCS_PROVIDERS_NORMAL=%TRACE_NOCS_PROVIDERS_NORMAL_NODXGIDEBUG%+%TRACE_DXGIDEBUG_NORMAL%")
        env.eval("TRACE_NOCS_PROVIDERS_VERBOSE=%TRACE_NOCS_PROVIDERS_VERBOSE_NODXGIDEBUG%+%TRACE_DXGIDEBUG_VERBOSE%")
        env.eval("TRACE_NT_MIN=LOADER+PROC_THREAD+CSWITCH+DISPATCHER+POWER")
        env.eval("TRACE_NT_LONGHAUL=LOADER+PROC_THREAD+POWER")
        env.eval("TRACE_NT_LIGHT=%TRACE_NT_MIN%+DISK_IO+HARD_FAULTS")
        env.eval("TRACE_NT_NORMAL=%TRACE_NT_LIGHT%+PROFILE+MEMINFO+DPC+INTERRUPT")
        env.eval("TRACE_NT_VERBOSE=%TRACE_NT_LIGHT%+PROFILE+MEMINFO+SYSCALL+DPC+INTERRUPT+ALL_FAULTS")

        # env.dump()
        self.env = env

    def start(self, mode="Normal"):
        if mode == "Min":
            self.env.eval("TRACE_NT_PROVIDER=%TRACE_NT_MIN%")
            self.env.eval("TRACE_CS_PROVIDERS=%TRACE_DXC_MIN%+%TRACE_CS_PROVIDERS_MIN%")
            self.env.eval("TRACE_CS_STATE=%TRACE_DXC_ALL%+%TRACE_CS_STATE_MIN%")
            self.env.eval("TRACE_NOCS_PROVIDERS=%TRACE_DX%:0x9+%TRACE_XAML%:4+%TRACE_WARP%:1+%TRACE_NOCS_PROVIDERS_MIN%")
        elif mode == "Present":
            self.env.eval("TRACE_NT_PROVIDER=%TRACE_NT_MIN%")
            self.env.eval("TRACE_CS_PROVIDERS=%TRACE_DXC_MIN%+%TRACE_CS_PROVIDERS_PRESENT%")
            self.env.eval("TRACE_CS_STATE=%TRACE_DXC_ALL_PRESENT%+%TRACE_CS_STATE_PRESENT%")
            self.env.eval("TRACE_NOCS_PROVIDERS=%TRACE_DX%:0x9+%TRACE_XAML%:4+%TRACE_NOCS_PROVIDERS_PRESENT%")
        elif mode == "Light":
            self.env.eval("TRACE_NT_PROVIDER=%TRACE_NT_LIGHT%")
            self.env.eval("TRACE_CS_PROVIDERS=%TRACE_DXC_LIGHT%+%TRACE_CS_PROVIDERS_LIGHT%")
            self.env.eval("TRACE_CS_STATE=%TRACE_DXC_ALL%+%TRACE_CS_STATE_LIGHT%")
            self.env.eval("TRACE_NOCS_PROVIDERS=%TRACE_DX%:0x2F+%TRACE_XAML%:4+%TRACE_WARP%:1+%TRACE_NOCS_PROVIDERS_LIGHT%")
        elif mode == "Normal":
            self.env.eval("TRACE_NT_PROVIDER=%TRACE_NT_NORMAL%")
            self.env.eval("TRACE_CS_PROVIDERS=%TRACE_DXC_NORMAL%+%TRACE_CS_PROVIDERS_NORMAL%")
            self.env.eval("TRACE_CS_STATE=%TRACE_DXC_ALL%+%TRACE_CS_STATE_NORMAL%")
            self.env.eval("TRACE_NOCS_PROVIDERS=%TRACE_DX%:0x2F+%TRACE_XAML%:4+%TRACE_WARP%:1+%TRACE_NOCS_PROVIDERS_NORMAL%+%TRACE_WDLOG_ERRORS%")
        else:
            self.env.eval("TRACE_NT_PROVIDER=%TRACE_NT_NORMAL%")
            self.env.eval("TRACE_CS_PROVIDERS=%TRACE_DXC_NORMAL%+%TRACE_CS_PROVIDERS_VERBOSE%")
            self.env.eval("TRACE_CS_STATE=%TRACE_DXC_ALL%+%TRACE_CS_STATE_VERBOSE%")
            self.env.eval("TRACE_NOCS_PROVIDERS=%TRACE_DX%+%TRACE_XAML%:5+%TRACE_WARP%:0x12+%TRACE_NOCS_PROVIDERS_VERBOSE%+%TRACE_WDLOG_ALL%")

        self.env.eval("TRACE_LARGE_BUFFERS=-BufferSize 1024 -MinBuffers 120 -MaxBuffers 480")

        cmds = [
            self.xperf_path + self.env.process(" -on %TRACE_NT_PROVIDER% %TRACE_LARGE_BUFFERS% -f Kernel.etl"),
            self.xperf_path + self.env.process(" -start CaptureState -on %TRACE_CS_PROVIDERS% %TRACE_LARGE_BUFFERS% -f CaptureState.etl"),
            self.xperf_path + self.env.process(" -capturestate CaptureState %TRACE_CS_STATE%"),
            self.xperf_path + self.env.process(" -start SchedulingLog -on %SCHEDULER_LOG_STATE% %TRACE_LARGE_BUFFERS% -f SchedulingLog.etl"),
            self.xperf_path + self.env.process(" -capturestate SchedulingLog %SCHEDULER_LOG_STATE%"),
            self.xperf_path + self.env.process(" -start NoCaptureState -on %TRACE_NOCS_PROVIDERS% %TRACE_LARGE_BUFFERS% -f NoCaptureState.etl")
        ]
        self.execute_cmds(cmds)

        print(" ### Start Profiling ###")

    def stop(self):
        cmds = [
            self.xperf_path + self.env.process(" -capturestate SchedulingLog %SCHEDULER_LOG_STATE%"),
            self.xperf_path + " -stop SchedulingLog",
            self.xperf_path + " -stop CaptureState",
            self.xperf_path + " -stop NoCaptureState",
            self.xperf_path + " -stop"
        ]
        self.execute_cmds(cmds)

        print(" ### Stop Profiling ###")

    def collect(self, path):
        cmds = [
            "rename CaptureState.etl, CaptureState2.etl",
            "rename Kernel.etl, Kernel2.etl",
            "rename NoCaptureState.etl, NoCaptureState2.etl",
            "rename SchedulingLog.etl, SchedulingLog2.etl",
            self.xperf_path + " -merge Kernel2.etl NoCaptureState2.etl CaptureState2.etl SchedulingLog2.etl %s" % path,
            self.xperf_path + " -setprofint",
            "del CaptureState2.etl",
            "del Kernel2.etl",
            "del NoCaptureState2.etl",
            "del SchedulingLog2.etl"
        ]
        self.execute_cmds(cmds)

    def collect_async(self, path):
        self.execute_cmds([
            "rename CaptureState.etl  CaptureState2.etl",
            "rename Kernel.etl Kernel2.etl",
            "rename NoCaptureState.etl NoCaptureState2.etl",
            "rename SchedulingLog.etl SchedulingLog2.etl"
        ])

        def do_merge_and_cleanup():
            self.execute_cmds([
                self.xperf_path + " -merge Kernel2.etl NoCaptureState2.etl CaptureState2.etl SchedulingLog2.etl %s" % path,
                self.xperf_path + " -setprofint",
                "del CaptureState2.etl",
                "del Kernel2.etl",
                "del NoCaptureState2.etl",
                "del SchedulingLog2.etl"
            ])

        new_thread = threading.Thread(target = do_merge_and_cleanup)
        new_thread.start()

    def execute_cmds(self, cmds):
        for cmd in cmds:
            print(cmd)
            os.system(cmd)

prof = Profiler("\"D:\\Windows Kits\\10\\Windows Performance Toolkit\\xperf.exe\"")

atexit.register(prof.stop)
while True:
    prof.start()
    time.sleep(15)
    prof.stop()
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    prof.collect_async(timestamp + ".etl")

