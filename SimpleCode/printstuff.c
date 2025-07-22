/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printstuff.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 19:49:21 by pinkwish          #+#    #+#             */
/*   Updated: 2025/07/22 11:49:00 by gzenner          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

int main()
{
    printf("%s", "Hello World.\n");
    
    //------------------------
    
    printf("%s %s", "Hello", "World.\n");
    
    //------------------------

    int i;
    
    i = 0;
    //while(i++ < 30)
    //    printf("%c", '=');
    printf("\n");
        
    //------------------------
    int j;
    i = 0;
    j = 0;
    /*while(j < 10)
    {
        i = 0;
        while(i++ < j)
        {
            printf("=");
        }
        printf("\n");
        ++j;
    }*/
    
    /*while(j > 0)
    {
        i = 0;
        while(i++ < j)
        {
            printf("=");
        }
        printf("\n");
        --j;
    }*/

    // ------
    //#Taking user input and printing it

    char buffer[50];

    /*i = 0;
    while(i < 50)
        buffer[i++] = 0;
    write(1, "Enter sth\n", 10);
    read(0, buffer, 49);
    write(1, buffer, 50);*/

    //#Taking Several Inputs, then printing them
    char inputs[3][50];
    
    i = 0;
    while(i < 3)
    {
        j = 0;
        while(j < 50)
        {
            inputs[i][j] = 0;
            ++j;
        }
        ++i;
    }

    i = 0;
    while(i < 3)
    {
        read(0, inputs[i], 49);
        write(1, inputs[i], 50);
        ++i;
    }
    return (0);
}