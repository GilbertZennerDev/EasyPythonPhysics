/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printstuff.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pinkwish <pinkwish@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 19:49:21 by pinkwish          #+#    #+#             */
/*   Updated: 2025/07/21 20:19:28 by pinkwish         ###   ########.fr       */
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
    while(j < 10)
    {
        i = 0;
        while(i++ < j)
        {
            printf("=");
        }
        printf("\n");
        ++j;
    }
    
    while(j > 0)
    {
        i = 0;
        while(i++ < j)
        {
            printf("=");
        }
        printf("\n");
        --j;
    }
       
    return (0);
}