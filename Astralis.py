def every_other_char(s):
    l = list(s)
    l = [c[1] for c in enumerate(l) if c[0] % 2 == 0]
    return "".join(l)


print(every_other_char("hello"))
print(every_other_char("hello"))

#include <stdio.h>
#include <string.h>
char* strdup_every_other_char(const char* s) {
int len = strlen(s);
int newLen = 0;
if (len % 2 == 0) {
newLen = len / 2 + 1;
}
else {
newLen = len / 2 + 2;
}
char* returnString = (char*) malloc(newLen * sizeof(char));
for (int i  = 0; i < newLen - 1; i++) {
returnString[i] = s[i * 2];
}
returnString[newLen -1] = '\0';
return returnString;
}