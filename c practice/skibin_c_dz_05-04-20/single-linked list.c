#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>


typedef struct island {
    int value;
    struct island *next;
} island;


island *make_first(int v)
{
    island *first = malloc(sizeof(island));

    first->value = v;
    first->next = NULL;

    return first;
};


void add_last(island *beg, int v){
    if(beg->next)
        add_last(beg->next, v);
    else{
        island *new = malloc(sizeof(island));
        beg->next = new;
        new->value = v;
        new->next = NULL;
    }
}


void displayR(const island *beg){
    beg ? printf("value: %d\n", beg->value), displayR(beg->next) : 0;
}


int del_end_el(island *beg, int n){
    if(beg->next){
        if(beg->next->next)
            del_end_el(beg->next, n+1);
        else{
            free(beg->next);
            beg->next = NULL;
            return n+1;
        }
    }
    else
        free(beg);
        return 0;
}


void del_all_lst(island *beg){
    if(beg->next){
        del_all_lst(beg->next);
        free(beg);
    }
    else
        free(beg);
}


int search(island *beg, int v, int i){
    if(beg->value != v){
        if(beg->next)
            search(beg->next, v, i+1);
        else
            return 0;
    }
    else
        return i+1;
};


int gui(){
    int on = 1;
    int lst, f, l;
    int t, n;
    island *x;

    while(on){

        switch(on){

        /* 1: main menu */
        case 1:
            printf("1: create list\n");
            printf("0: exit\n");

            printf(">>> ");
            t = scanf("%d", &n);
            if(t != 1){
                printf("------| error |------\n");
                printf("incorrect data have been entered\n");
                return 1;
            }

            switch(n){

            /* exit */
            case 0:
                on = 0;
                break;

            /* create list */
            case 1:
                printf(">>> enter the first element of list: ");
                t = scanf("%d", &n);
                if(t != 1){
                    printf("------| error |------\n");
                    printf("incorrect data have been entered\n");
                    return 1;
                }
                x = make_first(n);
                lst = l = 1;
                on = 2;
                break;

            default:
                printf("------| error |------\n");
                printf("incorrect data have been entered\n");
                printf("please, choose the one of listed actions\n");
            }
            printf("---------------------\n");
            break;

        /* 2: list manipulations */
        case 2:
            printf("1: add an element to end of list\n");
            printf("2: delete an end element of list\n");
            printf("3: find an element\n");
            printf("4: show the list\n");
            printf("5: delete the list\n");
            printf("0: exit\n");
            printf(">>> ");
            t = scanf("%d", &n);
               if(t != 1){
                    printf("------| error |------\n");
                    printf("incorrect data have been entered\n");
                    return 1;
                }

            switch(n){

            /* exit */
            case 0:
                if(lst)
                    del_all_lst(x);
                on = 0;
                printf("---------------------\n");
                break;

            /* add an element to end of list */
            case 1:
                printf(">>> enter the value of an adding element: ");
                t = scanf("%d", &n);
                if(t != 1){
                    printf("------| error |------\n");
                    printf("incorrect data have been entered\n");
                    return 1;
                }
                add_last(x, n);
                printf("---------------------\n");
                break;

            /* delete an end element of list */
            case 2:
                l = del_end_el(x, 0);
                if(!l){
                    printf(">>> the list has been deleted\n");
                    on = 1;
                }
                printf("---------------------\n");
                break;

            /* find an element */
            case 3:
                printf(">>> enter the value you want to find: ");
                t = scanf("%d", &n);
                if(t != 1){
                    printf("------| error |------\n");
                    printf("incorrect data have been entered\n");
                    return 1;
                }
                f = search(x, n, 0);
                if(f)
                    printf(">>> the index of %d is %d\n", n, f);
                else
                    printf(">>> no such value in the list\n");
                printf("---------------------\n");
                break;

            /* show the list */
            case 4:
                displayR(x);
                printf("---------------------\n");
                break;

            /* delete whole list */
            case 5:
                del_all_lst(x);
                printf(">>> the list has been deleted\n");
                on = 1;
                printf("---------------------\n");
                break;

            default:
                printf("------| error |------\n");
                printf("incorrect data have been entered\n");
                printf("please, choose the one of listed actions\n");

            printf("---------------------\n");
            break;
            }
        }
    }

    return 0;
}


int main()
{
    gui();

    return 0;
}
