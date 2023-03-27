#include <stdio.h>

int main(void)
{
    int x, y;
    int date;
    scanf("%d %d", &x, &y);
    if (x == 1)
        date = y;
    else if (x == 2)
        date = 31 + y;
    else if (x == 3)
        date = 59+ y;
    else if (x == 4)
        date = 90 + y;
    else if (x == 5)
        date = 120 + y;
    else if (x == 6)
        date = 151 + y;
    else if (x == 7)
        date = 181 + y;
    else if (x == 8)
        date = 212 + y;
    else if (x == 9)
        date = 243 + y;
    else if (x == 10)
        date = 273 + y;
    else if (x == 11)
        date = 304 + y;
    else if (x == 12)
        date = 334 + y;
    switch(date % 7){
    case 0 :
        printf("SUN");
        break ;
    case 1 :
        printf("MON");
        break ;
    case 2 :
        printf("TUE");
        break ;
    case 3 :
        printf("WED");
        break ;
    case 4 :
        printf("THU");
        break ;
    case 5 :
        printf("FRI");
        break ;
    case 6 :
        printf("SAT");
        break ;
    }
    return (0);
}
