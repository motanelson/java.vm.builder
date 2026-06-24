print("\033[47;31m\n\ngive me the string")

var0=input().strip()
var1=""
match var0:


    case "iadd":
        var1="mov eax,[esp+4];mov ebx,[esp+8];add eax,ebx"


    case "isub":
        var1="mov eax,[esp+4];mov ebx,[esp+8];sub eax,ebx"


    case "imul":
        var1="mov eax,[esp+4];mov ebx,[esp+8];mov ecx,0;mov edx,0;imul eax,ebx"


    case "idiv":
        var1="mov eax,[esp+4];mov ebx,[esp+8];mov ecx,0;mov edx,0;idiv eax,ebx"


print(var1)