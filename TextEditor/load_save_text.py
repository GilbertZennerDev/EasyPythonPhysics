# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_save_text.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pinkwish <pinkwish@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/19 21:45:59 by pinkwish          #+#    #+#              #
#    Updated: 2025/07/19 22:02:04 by pinkwish         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def loadText(filename):
    """Returns the content of the file with the given filename, or empty string if not found."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ''
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return ''

def saveText(filename, content):
    """Writes content to the file with the given filename."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error saving to {filename}: {e}")
