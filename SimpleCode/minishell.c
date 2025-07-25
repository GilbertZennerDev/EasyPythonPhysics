/* ************************************************************************** */
/*																			*/
/*														:::	  ::::::::   */
/*   mininano.c										 :+:	  :+:	:+:   */
/*													+:+ +:+		 +:+	 */
/*   By: gzenner <gzenner@student.42.fr>			+#+  +:+	   +#+		*/
/*												+#+#+#+#+#+   +#+		   */
/*   Created: 2025/07/24 17:58:17 by gzenner		   #+#	#+#			 */
/*   Updated: 2025/07/25 10:27:56 by gzenner		  ###   ########.fr	   */
/*																			*/
/* ************************************************************************** */

#include <unistd.h>
#include <sys/wait.h>
#include "/home/gzenner/active/libft/libft.h"

#define LINE_BUFFER 1024

void minicalloc(char input_buffer[], unsigned int limit)
{
	unsigned int i;

	i = 0;
	while(i < limit)
		input_buffer[i++] = 0;
}

typedef struct s_data
{
	char input_buffer[1024];
	char *newdir;
	char *cmd;
	pid_t pid;
}   t_data;

void runchild(t_data data)
{
	data.pid = fork();
	if (data.pid < 0)
	{
		ft_putstr_fd("Fork Error\n", 2);
	}
	else if (data.pid == 0)
	{
		extern char **environ;
		const char *cmds[] = {ft_strjoin("/bin/", data.cmd), NULL};
		execve(cmds[0], (char* const*)cmds, environ);
		ft_putstr_fd("Unknown Command\n", 2);
	}
	else
	{
		wait(NULL);
	}
}

int main()
{
	t_data data;

	minicalloc(data.input_buffer, LINE_BUFFER);
	while (ft_strcmp(data.input_buffer, "exit\n"))
	{
		minicalloc(data.input_buffer, LINE_BUFFER);
		read(0, data.input_buffer, 1024);
		if (ft_strncmp(data.input_buffer, "cd ", 3) == 0)
		{
			data.newdir = ft_substr(data.input_buffer, 3, ft_strlen(data.input_buffer)-4);
			if (chdir(data.newdir) == -1)
				ft_putstr_fd("Error CD\n", 2);
		}
		else if (ft_strcmp(data.input_buffer, "pwd\n") == 0)
		{
			minicalloc(data.input_buffer, LINE_BUFFER);
			getcwd(data.input_buffer, 1024);
			ft_printf("%s\n", data.input_buffer);
		}
		else if (ft_strcmp(data.input_buffer, "exit\n") == 0)
		{
			break;
		}
		else
		{
			data.cmd = ft_substr(data.input_buffer, 0, ft_strlen(data.input_buffer)-1);
			runchild(data);
		}
		/*
		if (ft_strcmp(data.input_buffer, "clear\n") == 0)
		{
			runchild(data, "clear");
		}*/
	}
	return (0);
}