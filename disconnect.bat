for /f "skip=1 tokens=3" %%s in ('query user 'johnny.abouhaidar') do (

%windir%\System32\tscon.exe %%s /dest:console

)

pause