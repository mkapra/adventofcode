#!/usr/bin/perl

use strict;
use warnings;

my $counter = 0;

my $file = "../../passwords.txt";
open(FH, $file) or die("Could not open file: $!");

foreach my $line (<FH>) {
	if ($line =~ /(\d*)-(\d*) (\w): (\w*)/) {
		my $min = $1;
		my $max = $2;
		my $char = $3;
		my $pass = $4;

		my $charCounter = 0;
		my $offset = 0;
		my $result = index($pass, $char, $offset);
		while ($result != -1) {
			$charCounter++;
			$offset = $result + 1;
			$result = index($pass, $char, $offset);
		}

		if ($charCounter >= $min && $charCounter <= $max) {
			$counter++;
		}
	}
}

close(FH);

print("Valid passwords: ${counter}\n");
