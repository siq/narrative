#!/bin/bash
interpolate() {
  perl -p -e 's/\$\{([^}]+)\}/defined $ENV{$1} ? $ENV{$1} : $&/eg; s/\$\{([^}]+)\}//eg' $1 > $2 
}

$(find -L $BUILDPATH -type f -executable -name python) setup.py install

interpolate pkg/narrative.yaml narrative.yaml.install
install -D -m 0644 narrative.yaml.install $BUILDPATH$SVCPATH/narrative/narrative.yaml

interpolate pkg/logrotate.conf logrotate.conf.install
install -D -m 0644 logrotate.conf.install $BUILDPATH/etc/logrotate.d/siq-narrative
