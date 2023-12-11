#include <unistd.h>

void	ft_putstr(char *str)
{
	while(*str != '\0')
	{
		write(1, str, 1);
		str++;
	}
	write(1, "\n", 1);
}

int main(int ac, char **av)
{
	if (ac != 2)
	{
		ft_putstr("error, insert one param\n");
		return (1);
	}
	else
	{
		ft_putstr(av[1]);
	}
	return (0);
}
