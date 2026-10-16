#!/usr/bin/env python3
"""Check macOS GUI service access before launching a native browser.

Usage: python3 scripts/macos-gui-preflight.py [-- COMMAND [ARG ...]]
This checks the caller's execution context; it never changes permissions.
"""

import ctypes
import os
import sys


def main():
    args = sys.argv[1:]
    if args and (args[0] != "--" or len(args) == 1):
        print(__doc__, file=sys.stderr)
        return 2
    if sys.platform == "darwin":
        lib = ctypes.CDLL("/usr/lib/libSystem.B.dylib")
        lib.bootstrap_look_up.argtypes = [ctypes.c_uint, ctypes.c_char_p,
                                         ctypes.POINTER(ctypes.c_uint)]
        lib.bootstrap_look_up.restype = ctypes.c_int
        lib.mach_task_self.restype = ctypes.c_uint
        lib.mach_port_deallocate.argtypes = [ctypes.c_uint, ctypes.c_uint]
        bootstrap = ctypes.c_uint.in_dll(lib, "bootstrap_port").value
        failed = []
        for service in ("com.apple.coreservices.launchservicesd",
                        "com.apple.windowserver.active"):
            port = ctypes.c_uint()
            result = lib.bootstrap_look_up(bootstrap, service.encode(),
                                           ctypes.byref(port))
            if result:
                failed.append(f"{service} (Mach error {result})")
            else:
                lib.mach_port_deallocate(lib.mach_task_self(), port.value)
        if failed:
            print("Native browser launch blocked: " + "; ".join(failed),
                  file=sys.stderr)
            print("Use an available browser tool or an execution context already "
                  "permitted by the task. Do not retry Chrome here: it can abort "
                  "during macOS application registration. --no-sandbox does not "
                  "change the parent shell's restrictions.", file=sys.stderr)
            return 77
    if args:
        os.execvp(args[1], args[1:])
    print("macOS GUI service preflight passed" if sys.platform == "darwin"
          else "macOS GUI service preflight not needed on this platform")
    return 0


if __name__ == "__main__":
    sys.exit(main())
