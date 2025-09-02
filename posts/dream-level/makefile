setup:
	npm install -g svgo

build: dream.svg level.svg

%_clean.svg: %_sketch.svg
	svgo $^ --pretty -o $@

%.svg: %_clean.svg generate.py
	python3 generate.py $^ > $@

dream_level.zip: \
		dream_clean.svg dream_sketch.svg dream.svg \
		level_clean.svg level_sketch.svg level.svg \
		generate.py
	zip $@ $^
