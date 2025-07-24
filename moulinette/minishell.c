/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   minishell.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 14:00:52 by gzenner           #+#    #+#             */
/*   Updated: 2025/07/24 14:10:57 by gzenner          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>

int main()
{
    const char *cmds[]={"/bin/ls", "-l", NULL};
    pid_t pid = fork();
    if (pid < 0)
    {
        printf("Fork Error\n");
        exit(1);
    }
    else if (pid == 0)
    {
        printf("Running Child.\n");
        execve(cmds[0], (char* const*)cmds, NULL);
    }
    else
    {
        wait(NULL);
        printf("Child Done\n");
    }   
    return (0);
}