chcp 65001
rem @echo off
setlocal EnableDelayedExpansion

set hh=%TIME:~0,2%
set mm=%TIME:~3,2%
set ss=%TIME:~6,2%
echo %hh%:%mm%:%ss% %DATE% > ".\Анализ\log.txt"
echo ------------------------------------------- >> ".\Анализ\log.txt"

set n=%~1
if %n%=="" (set n=10)

for /L %%i in (1,1,%n%) do (
    set "formattedValue=000000%%i"

	echo %%i >> ".\Анализ\log.txt"
	(copy /y/v ".\Магазин%%i\in.txt" ".\Анализ\store!formattedValue:~-3!_in.txt") >> ".\Анализ\log.txt"
	(copy /y/v ".\Магазин%%i\out.txt" ".\Анализ\store!formattedValue:~-3!_out.txt") >> ".\Анализ\log.txt"
)
