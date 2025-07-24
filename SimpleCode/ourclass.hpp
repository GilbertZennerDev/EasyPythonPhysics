/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ourclass.hpp                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 13:34:50 by gzenner           #+#    #+#             */
/*   Updated: 2025/07/24 13:36:49 by gzenner          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

class OurClass
{
    private:
        unsigned int participants;
    public:
        OurClass(unsigned int);
        ~OurClass();
        unsigned int getParticipants();
        void setParticipants();
}