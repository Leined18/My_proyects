#include <stdio.h>
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	int i = 0;
	while(*str != '\0')
	{
		ft_putchar(str);
		str++;
	}
}

int main(int ac, char **av)
{
	if (ac != 2)
		ft_putstr("Escribe solo un argumento\n");
	while(av[1] == '\0')
	{
		if (av[1] >= 'a' && av[1] <= 'z')
		{
			av[1] += 32;
			ft_putchar(av);
			av++;
		}
		av++;
	}
	return (0);
}
