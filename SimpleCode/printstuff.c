/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printstuff.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 19:49:21 by pinkwish          #+#    #+#             */
/*   Updated: 2025/07/24 13:33:15 by gzenner          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdbool.h>

bool isEven(int nb)
{
    return (!(nb%2));
}

int ft_atoi(const char *nb)
{
    unsigned int i;
    int result;

    i = 0;
    result = 0;
    while(nb[i] != 0)
    {
        result = 10*result + (nb[i] - '0');
        ++i;
    }
    return (result);
}

void ft_putnbr(int nb)
{    
    if (nb < 0)
    {
        printf("-");
        nb *= -1;
    }
    if (nb > 10)
        ft_putnbr(nb / 10);
    printf("%c", "0123456789"[nb % 10]);
}

int main()
{
    ft_putnbr(-1234);
    return (0);
}