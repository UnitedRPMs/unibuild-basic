Name:           unibuild-basic
Summary:        unibuild-basic metapackage
License:	LGPLv3
Source0: 	https://www.gnu.org/licenses/lgpl-3.0.txt
Version:        0.1
Release:        1%{dist}
Url:            https://unitedrpms.github.io/
Requires:	x264
Requires:	x265
Requires:	lame
Requires:	a52dec
Requires:	libbluray
Requires:	xvidcore
Requires:	faad2
Requires:	libdca
Requires:	live555
Requires:	mpeg2dec
Requires:	twolame
Requires:	vcdimager
Requires:	aften
Requires:	opencore-amr
Requires:	faac
Requires:	libmms
Requires:	rtmpdump
Requires:	libmpeg2
Requires:	libquicktime
Requires:	nvenc
Requires:	mjpegtools
Requires:	libmng
Requires:	libdvdcss
Requires:	vo-aacenc
Requires:	vo-amrwbenc	  

%description
This is a metapaquete, for the basic construction in URPMS. 
Specifically for a massive rebuild of packages by a release change. 


%prep

# Nothing here

%build

# Nothing here

%install

# Nothing here

%files
# Nothing here

%changelog

* Tue Apr 04 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1-1
- Initial build
