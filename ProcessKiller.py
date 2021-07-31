import ctypes

print("Process-Killer Build 1 By Nort721\n")

percentage = "0%"

user_handle = ctypes.WinDLL("User32.dll")
kernel_handle = ctypes.WinDLL("Kernel32.dll")

while True:
    lpWindowName = ctypes.c_char_p(input("Enter window name: ").encode('utf-8'))

    print("Terminating process . . . 0%")

    hWnd = user_handle.FindWindowA(None, lpWindowName)

    if hWnd == 0:
        print("Error code: {0}, could not find window".format(kernel_handle.GetLastError()))
        continue
    else:
        print("Terminating process . . . 25%")

    lpdwProcessId = ctypes.c_ulong()

    response = user_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

    if response == 0:
        print("Error code: {0}, could not get PID".format(kernel_handle.GetLastError()))
        continue
    else:
        print("Terminating process . . . 50%")

    dwDesiredAccess = 0x0001
    dwProcessId = lpdwProcessId

    hProcess = kernel_handle.OpenProcess(dwDesiredAccess, False, dwProcessId)
    uExitCode = 0x1

    if hProcess == 0:
        print("Error code: {0}, could not open the process".format(kernel_handle.GetLastError()))
        continue
    else:
        print("Terminating process . . . 75%")

    response = kernel_handle.TerminateProcess(hProcess, uExitCode)

    if response == 0:
        print("Error code: {0}, could not terminate process".format(kernel_handle.GetLastError()))
        continue
    else:
        print("Terminating process . . . 100%")
        print("Process terminated successfully!")

    print()

