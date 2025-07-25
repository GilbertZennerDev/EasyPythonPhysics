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

void minicalloc_inputbuffer(char input_buffer[], unsigned int limit)
{
	unsigned int i;

	i = 0;
	while(i < limit)
		input_buffer[i++] = 0;
}

void minicalloc_filebuffer(char file_buffer[LINE_BUFFER][LINE_BUFFER], unsigned int limit)
{
	unsigned int i;
	unsigned int j;

	i = 0;
	while(i < limit)
	{
		j = 0;
		while(j < limit)
		{
			file_buffer[i][j++] = 0;
		}
		++i;
	}
		
}

typedef struct s_data
{
	char input_buffer[1024];
	char file_buffer[1024][1024];
	unsigned int line_index;
}   t_data;

void init_data(t_data *data)
{
	minicalloc_inputbuffer(data->input_buffer, LINE_BUFFER);
	minicalloc_filebuffer(data->file_buffer, LINE_BUFFER);
	data->line_index = 0;
}

int main()
{
	t_data data;

	init_data(&data);
	while (ft_strcmp(data.input_buffer, "exit\n") != 0)
	{
		minicalloc_inputbuffer(data.input_buffer, LINE_BUFFER);
		read(0, data.input_buffer, 1024);
		if (ft_strcmp(data.input_buffer, "save\n") == 0)
		{
			printf("dummy file saved");
		}
		else if (ft_strcmp(data.input_buffer, "load\n") == 0)
		{
			printf("dummy file loaded");
		}
		else if (ft_strcmp(data.input_buffer, "exit\n") == 0)
		{
			break;
		}
		else
		{
			ft_memcpy(data.file_buffer[data.line_index], data.input_buffer, ft_strlen(data.input_buffer));
		}
	}
	return (0);
}