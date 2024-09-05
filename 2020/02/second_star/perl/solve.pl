#!/usr/bin/perl

use strict;
use warnings;

my $counter = 0;

my $file = "../../passwords.txt";
open(FH, $file) or die("Could not open file: $!");

foreach my $line (<FH>) {
	if ($line =~ /(\d*)-(\d*) (\w): (\w*)/) {
		my $index_first = $1;
		my $index_second = $2;
		my $char = $3;
		my $pass = $4;

		my $first_index_char = substr($pass, $index_first - 1, 1);
		my $second_index_char = substr($pass, $index_second - 1, 1);

		if (($first_index_char eq $char) xor ($second_index_char eq $char)) {
			$counter++;
		}
	}
}

close(FH);

print("Valid passwords: ${counter}\n");
