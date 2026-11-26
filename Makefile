new-day-%:
	@echo "Creating day $*"
	mkdir -p aoc-2026-inputs/day-$*/
	touch aoc-2026-inputs/day-$*/input.txt
	touch aoc-2026-inputs/day-$*/test.txt
	cp -r template-day day-$*
	@echo "Done. Happy coding!"
