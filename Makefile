# This Makefile automates certain tasks, such as
# individual documentation for projects

doc:
	cd $(proyecto)
	sphinx-quickstart sphinx-quickstart . --author "Alexander Calderón Torres" --project  -q