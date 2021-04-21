# UMATT-dev

## **TODO:**
- [ ] Figure out the mappings from wirePi to the `P20 Control Board`
- [ ] Find coding standard, document then implement
- [ ] Begin creation of documentation (Markdown)
	- [ ] This README.md needs to have a project introduction and some navigation integrated.
	- Be sure to read [THIS ARTICLE](https://documentation.divio.com) to understand what kind of documentation you're actually looking to create.
- [ ] Add comments to code for clairity (Andrew/Rita ask, Kathrine supplements?)
- [ ] Implement GUI lib and starter interface
	- [ ] Document interaction between logic and ui layers thoroughly.
- [ ] Configure, Document and implement main drive state machine.
- [ ] Document environment setup for project.
	- [ ] rpi setup (from fresh rpiOS to running tractor)
	- [ ] Win10, MacOS, Nix development environments
	- [ ] Win10, MacOS, Nix LVGL simulation environments?




# Running the Project

## Hook er up

- Power
//TODO: Kathrine did I get these board names correct? Also, what other steps should we include here? (do we want to include the board wiring diagrams in this repo?)
- Correctly to the GPIO Pins to the `P20 Control board`
- Correctly `P20 Control Board` to `P20 Relay Board`

## Compilation

The project comes with a ready to use `makefile`. It's quite simple in nature, linking and compiling all files in `/src/` to `/object/` and then everything is rounded up in an executable named `UMATT_main` on successful build.
(WARNING: If your build fails the `UMATT_main` file will not be updated since it was last successfully built.)

To use simply run `make` in the project root and keep an eye on the build for errors, on success you get a message referring to the freshly built executable.
Running `make clean` will remove all the temp files in `/object/` and the executable file, essentially cleaning up the workspace.

## Running

Currently we're in the testing phases so the board is on das blinkin lights mode. Simply run the executable in terminal with `UMATT_main`
