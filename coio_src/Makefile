PYTHON=stackless2.6

# Ignoring DeprecationWarning since Pyrex does an `import md5'
PYREXC=$(PYTHON) -W ignore::DeprecationWarning -c "from Pyrex.Compiler.Main import main; from Pyrex.Compiler.Errors import warnings_issued; warnings_issued['or_none'] = 1; main(command_line=1)"
# Anything before 0.9.9 is not good enugh, because it has the exception
# handling bug
# http://code.google.com/p/pts-mini-gpl/source/browse/trunk/excbug/README.txt
PYREX_MIN_VERSION=0.9.9
PYREX_CHECKVERSION=$(PYTHON) -W ignore::DeprecationWarning -c "from Pyrex.Compiler.Version import version; min_version = '$(PYREX_MIN_VERSION)'; assert version >= min_version, 'please upgrade your Pyrex to >= %s' % min_version"
CYTHON=$(PYTHON) -c "from Cython.Compiler.Main import main; main(command_line = 1)"

.PHONY: all install clean

all: coio.c
	cd .. && $(PYTHON) setup.py build

install:
	cd .. && $(PYTHON) setup.py install

clean:
	cd .. && $(PYTHON) setup.py clean
	rm -rf ../build

# Doesn't work yet.
#test:
#	$(PYTHON) test.py

# Compile with Cython instead of Pyrex because Pyrex has the bug
# http://code.google.com/p/pts-mini-gpl/source/browse/trunk/excbug/README.txt
coio.c: coio.pyx event.pxi nbevent.pxi evdns.pxi
	$(PYREX_CHECKVERSION)
	$(PYREXC) coio.pyx
	#$(CYTHON) coio.pyx