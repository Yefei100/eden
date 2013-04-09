#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of the web2py Web Framework
Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

CONTENT_TYPE dictionary created against freedesktop.org' shared mime info
database version 1.1.

Deviations from official standards:
- '.md': 'application/x-genesis-rom' --> 'text/x-markdown'
- '.png': 'image/x-apple-ios-png' --> 'image/png'
Additions:
- '.load': 'text/html'
- '.json': 'application/json'
- '.jsonp': 'application/jsonp'
- '.pickle': 'application/python-pickle'
- '.w2p': 'application/w2p'
"""

__all__ = ['contenttype']

CONTENT_TYPE = {
    '.123': 'application/vnd.lotus-1-2-3',
    '.3ds': 'image/x-3ds',
    '.3g2': 'video/3gpp2',
    '.3ga': 'video/3gpp',
    '.3gp': 'video/3gpp',
    '.3gp2': 'video/3gpp2',
    '.3gpp': 'video/3gpp',
    '.3gpp2': 'video/3gpp2',
    '.602': 'application/x-t602',
    '.669': 'audio/x-mod',
    '.7z': 'application/x-7z-compressed',
    '.a': 'application/x-archive',
    '.aac': 'audio/aac',
    '.abw': 'application/x-abiword',
    '.abw.crashed': 'application/x-abiword',
    '.abw.gz': 'application/x-abiword',
    '.ac3': 'audio/ac3',
    '.ace': 'application/x-ace',
    '.adb': 'text/x-adasrc',
    '.ads': 'text/x-adasrc',
    '.afm': 'application/x-font-afm',
    '.ag': 'image/x-applix-graphics',
    '.ai': 'application/illustrator',
    '.aif': 'audio/x-aiff',
    '.aifc': 'audio/x-aifc',
    '.aiff': 'audio/x-aiff',
    '.aiffc': 'audio/x-aifc',
    '.al': 'application/x-perl',
    '.alz': 'application/x-alz',
    '.amr': 'audio/amr',
    '.amz': 'audio/x-amzxml',
    '.ani': 'application/x-navi-animation',
    '.anim[1-9j]': 'video/x-anim',
    '.anx': 'application/annodex',
    '.ape': 'audio/x-ape',
    '.apk': 'application/vnd.android.package-archive',
    '.ar': 'application/x-archive',
    '.arj': 'application/x-arj',
    '.arw': 'image/x-sony-arw',
    '.as': 'application/x-applix-spreadsheet',
    '.asc': 'text/plain',
    '.asf': 'video/x-ms-asf',
    '.asp': 'application/x-asp',
    '.ass': 'text/x-ssa',
    '.asx': 'audio/x-ms-asx',
    '.atom': 'application/atom+xml',
    '.au': 'audio/basic',
    '.avf': 'video/x-msvideo',
    '.avi': 'video/x-msvideo',
    '.aw': 'application/x-applix-word',
    '.awb': 'audio/amr-wb',
    '.awk': 'application/x-awk',
    '.axa': 'audio/annodex',
    '.axv': 'video/annodex',
    '.bak': 'application/x-trash',
    '.bcpio': 'application/x-bcpio',
    '.bdf': 'application/x-font-bdf',
    '.bdm': 'video/mp2t',
    '.bdmv': 'video/mp2t',
    '.bib': 'text/x-bibtex',
    '.bin': 'application/octet-stream',
    '.blend': 'application/x-blender',
    '.blender': 'application/x-blender',
    '.bmp': 'image/bmp',
    '.bz': 'application/x-bzip',
    '.bz2': 'application/x-bzip',
    '.c': 'text/x-csrc',
    '.c++': 'text/x-c++src',
    '.cab': 'application/vnd.ms-cab-compressed',
    '.cap': 'application/vnd.tcpdump.pcap',
    '.cb7': 'application/x-cb7',
    '.cbl': 'text/x-cobol',
    '.cbr': 'application/x-cbr',
    '.cbt': 'application/x-cbt',
    '.cbz': 'application/x-cbz',
    '.cc': 'text/x-c++src',
    '.ccmx': 'application/x-ccmx',
    '.cdf': 'application/x-netcdf',
    '.cdr': 'application/vnd.corel-draw',
    '.cer': 'application/pkix-cert',
    '.cert': 'application/x-x509-ca-cert',
    '.cgm': 'image/cgm',
    '.chm': 'application/vnd.ms-htmlhelp',
    '.chrt': 'application/x-kchart',
    '.class': 'application/x-java',
    '.clpi': 'video/mp2t',
    '.cls': 'text/x-tex',
    '.cmake': 'text/x-cmake',
    '.cob': 'text/x-cobol',
    '.cpi': 'video/mp2t',
    '.cpio': 'application/x-cpio',
    '.cpio.gz': 'application/x-cpio-compressed',
    '.cpp': 'text/x-c++src',
    '.cr2': 'image/x-canon-cr2',
    '.crl': 'application/pkix-crl',
    '.crt': 'application/x-x509-ca-cert',
    '.crw': 'image/x-canon-crw',
    '.cs': 'text/x-csharp',
    '.csh': 'application/x-csh',
    '.css': 'text/css',
    '.cssl': 'text/css',
    '.csv': 'text/csv',
    '.cue': 'application/x-cue',
    '.cur': 'image/x-win-bitmap',
    '.cxx': 'text/x-c++src',
    '.d': 'text/x-dsrc',
    '.dar': 'application/x-dar',
    '.dbf': 'application/x-dbf',
    '.dc': 'application/x-dc-rom',
    '.dcl': 'text/x-dcl',
    '.dcm': 'application/dicom',
    '.dcr': 'image/x-kodak-dcr',
    '.dds': 'image/x-dds',
    '.deb': 'application/x-deb',
    '.der': 'application/x-x509-ca-cert',
    '.desktop': 'application/x-desktop',
    '.di': 'text/x-dsrc',
    '.dia': 'application/x-dia-diagram',
    '.diff': 'text/x-patch',
    '.divx': 'video/x-msvideo',
    '.djv': 'image/vnd.djvu',
    '.djvu': 'image/vnd.djvu',
    '.dmg': 'application/x-apple-diskimage',
    '.dmp': 'application/vnd.tcpdump.pcap',
    '.dng': 'image/x-adobe-dng',
    '.doc': 'application/msword',
    '.docbook': 'application/x-docbook+xml',
    '.docm': 'application/vnd.ms-word.document.macroenabled.12',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.dot': 'text/vnd.graphviz',
    '.dotm': 'application/vnd.ms-word.template.macroenabled.12',
    '.dotx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.template',
    '.dsl': 'text/x-dsl',
    '.dtd': 'application/xml-dtd',
    '.dts': 'audio/vnd.dts',
    '.dtshd': 'audio/vnd.dts.hd',
    '.dtx': 'text/x-tex',
    '.dv': 'video/dv',
    '.dvi': 'application/x-dvi',
    '.dvi.bz2': 'application/x-bzdvi',
    '.dvi.gz': 'application/x-gzdvi',
    '.dwg': 'image/vnd.dwg',
    '.dxf': 'image/vnd.dxf',
    '.e': 'text/x-eiffel',
    '.egon': 'application/x-egon',
    '.eif': 'text/x-eiffel',
    '.el': 'text/x-emacs-lisp',
    '.emf': 'image/x-emf',
    '.eml': 'message/rfc822',
    '.emp': 'application/vnd.emusic-emusic_package',
    '.ent': 'application/xml-external-parsed-entity',
    '.eps': 'image/x-eps',
    '.eps.bz2': 'image/x-bzeps',
    '.eps.gz': 'image/x-gzeps',
    '.epsf': 'image/x-eps',
    '.epsf.bz2': 'image/x-bzeps',
    '.epsf.gz': 'image/x-gzeps',
    '.epsi': 'image/x-eps',
    '.epsi.bz2': 'image/x-bzeps',
    '.epsi.gz': 'image/x-gzeps',
    '.epub': 'application/epub+zip',
    '.erl': 'text/x-erlang',
    '.es': 'application/ecmascript',
    '.etheme': 'application/x-e-theme',
    '.etx': 'text/x-setext',
    '.exe': 'application/x-ms-dos-executable',
    '.exr': 'image/x-exr',
    '.ez': 'application/andrew-inset',
    '.f': 'text/x-fortran',
    '.f4a': 'audio/mp4',
    '.f4b': 'audio/x-m4b',
    '.f4v': 'video/mp4',
    '.f90': 'text/x-fortran',
    '.f95': 'text/x-fortran',
    '.fb2': 'application/x-fictionbook+xml',
    '.fig': 'image/x-xfig',
    '.fits': 'image/fits',
    '.fl': 'application/x-fluid',
    '.flac': 'audio/flac',
    '.flc': 'video/x-flic',
    '.fli': 'video/x-flic',
    '.flv': 'video/x-flv',
    '.flw': 'application/x-kivio',
    '.fo': 'text/x-xslfo',
    '.fodg': 'application/vnd.oasis.opendocument.graphics-flat-xml',
    '.fodp': 'application/vnd.oasis.opendocument.presentation-flat-xml',
    '.fods': 'application/vnd.oasis.opendocument.spreadsheet-flat-xml',
    '.fodt': 'application/vnd.oasis.opendocument.text-flat-xml',
    '.for': 'text/x-fortran',
    '.fxm': 'video/x-javafx',
    '.g3': 'image/fax-g3',
    '.gb': 'application/x-gameboy-rom',
    '.gba': 'application/x-gba-rom',
    '.gcrd': 'text/vcard',
    '.ged': 'application/x-gedcom',
    '.gedcom': 'application/x-gedcom',
    '.gem': 'application/x-tar',
    '.gen': 'application/x-genesis-rom',
    '.gf': 'application/x-tex-gf',
    '.gg': 'application/x-sms-rom',
    '.gif': 'image/gif',
    '.glade': 'application/x-glade',
    '.gml': 'application/gml+xml',
    '.gmo': 'application/x-gettext-translation',
    '.gnc': 'application/x-gnucash',
    '.gnd': 'application/gnunet-directory',
    '.gnucash': 'application/x-gnucash',
    '.gnumeric': 'application/x-gnumeric',
    '.gnuplot': 'application/x-gnuplot',
    '.go': 'text/x-go',
    '.gp': 'application/x-gnuplot',
    '.gpg': 'application/pgp-encrypted',
    '.gplt': 'application/x-gnuplot',
    '.gra': 'application/x-graphite',
    '.gsf': 'application/x-font-type1',
    '.gsm': 'audio/x-gsm',
    '.gtar': 'application/x-tar',
    '.gv': 'text/vnd.graphviz',
    '.gvp': 'text/x-google-video-pointer',
    '.gz': 'application/gzip',
    '.h': 'text/x-chdr',
    '.h++': 'text/x-c++hdr',
    '.h4': 'application/x-hdf',
    '.h5': 'application/x-hdf',
    '.hdf': 'application/x-hdf',
    '.hdf4': 'application/x-hdf',
    '.hdf5': 'application/x-hdf',
    '.hh': 'text/x-c++hdr',
    '.hlp': 'application/winhlp',
    '.hp': 'text/x-c++hdr',
    '.hpgl': 'application/vnd.hp-hpgl',
    '.hpp': 'text/x-c++hdr',
    '.hs': 'text/x-haskell',
    '.htm': 'text/html',
    '.html': 'text/html',
    '.hwp': 'application/x-hwp',
    '.hwt': 'application/x-hwt',
    '.hxx': 'text/x-c++hdr',
    '.ica': 'application/x-ica',
    '.icb': 'image/x-tga',
    '.icc': 'application/vnd.iccprofile',
    '.icm': 'application/vnd.iccprofile',
    '.icns': 'image/x-icns',
    '.ico': 'image/vnd.microsoft.icon',
    '.ics': 'text/calendar',
    '.idl': 'text/x-idl',
    '.ief': 'image/ief',
    '.iff': 'image/x-ilbm',
    '.ilbm': 'image/x-ilbm',
    '.ime': 'text/x-imelody',
    '.imy': 'text/x-imelody',
    '.ins': 'text/x-tex',
    '.iptables': 'text/x-iptables',
    '.iso': 'application/x-cd-image',
    '.iso9660': 'application/x-cd-image',
    '.it': 'audio/x-it',
    '.it87': 'application/x-it87',
    '.j2k': 'image/jp2',
    '.jad': 'text/vnd.sun.j2me.app-descriptor',
    '.jar': 'application/x-java-archive',
    '.java': 'text/x-java',
    '.jceks': 'application/x-java-jce-keystore',
    '.jks': 'application/x-java-keystore',
    '.jng': 'image/x-jng',
    '.jnlp': 'application/x-java-jnlp-file',
    '.jp2': 'image/jp2',
    '.jpc': 'image/jp2',
    '.jpe': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.jpf': 'image/jp2',
    '.jpg': 'image/jpeg',
    '.jpr': 'application/x-jbuilder-project',
    '.jpx': 'image/jp2',
    '.js': 'application/javascript',
    '.json': 'application/json',
    '.jsonp': 'application/jsonp',
    '.k25': 'image/x-kodak-k25',
    '.kar': 'audio/midi',
    '.karbon': 'application/x-karbon',
    '.kdc': 'image/x-kodak-kdc',
    '.kdelnk': 'application/x-desktop',
    '.kexi': 'application/x-kexiproject-sqlite3',
    '.kexic': 'application/x-kexi-connectiondata',
    '.kexis': 'application/x-kexiproject-shortcut',
    '.kfo': 'application/x-kformula',
    '.kil': 'application/x-killustrator',
    '.kino': 'application/smil',
    '.kml': 'application/vnd.google-earth.kml+xml',
    '.kmz': 'application/vnd.google-earth.kmz',
    '.kon': 'application/x-kontour',
    '.kpm': 'application/x-kpovmodeler',
    '.kpr': 'application/x-kpresenter',
    '.kpt': 'application/x-kpresenter',
    '.kra': 'application/x-krita',
    '.ks': 'application/x-java-keystore',
    '.ksp': 'application/x-kspread',
    '.kud': 'application/x-kugar',
    '.kwd': 'application/x-kword',
    '.kwt': 'application/x-kword',
    '.la': 'application/x-shared-library-la',
    '.latex': 'text/x-tex',
    '.lbm': 'image/x-ilbm',
    '.ldif': 'text/x-ldif',
    '.lha': 'application/x-lha',
    '.lhs': 'text/x-literate-haskell',
    '.lhz': 'application/x-lhz',
    '.load' : 'text/html',
    '.log': 'text/x-log',
    '.lrz': 'application/x-lrzip',
    '.ltx': 'text/x-tex',
    '.lua': 'text/x-lua',
    '.lwo': 'image/x-lwo',
    '.lwob': 'image/x-lwo',
    '.lwp': 'application/vnd.lotus-wordpro',
    '.lws': 'image/x-lws',
    '.ly': 'text/x-lilypond',
    '.lyx': 'application/x-lyx',
    '.lz': 'application/x-lzip',
    '.lzh': 'application/x-lha',
    '.lzma': 'application/x-lzma',
    '.lzo': 'application/x-lzop',
    '.m': 'text/x-matlab',
    '.m15': 'audio/x-mod',
    '.m1u': 'video/vnd.mpegurl',
    '.m2t': 'video/mp2t',
    '.m2ts': 'video/mp2t',
    '.m3u': 'application/vnd.apple.mpegurl',
    '.m3u8': 'application/vnd.apple.mpegurl',
    '.m4': 'application/x-m4',
    '.m4a': 'audio/mp4',
    '.m4b': 'audio/x-m4b',
    '.m4u': 'video/vnd.mpegurl',
    '.m4v': 'video/mp4',
    '.mab': 'application/x-markaby',
    '.mak': 'text/x-makefile',
    '.man': 'application/x-troff-man',
    '.manifest': 'text/cache-manifest',
    '.markdown': 'text/x-markdown',
    '.mbox': 'application/mbox',
    '.md': 'text/x-markdown',
    '.mdb': 'application/vnd.ms-access',
    '.mdi': 'image/vnd.ms-modi',
    '.me': 'text/x-troff-me',
    '.med': 'audio/x-mod',
    '.meta4': 'application/metalink4+xml',
    '.metalink': 'application/metalink+xml',
    '.mgp': 'application/x-magicpoint',
    '.mht': 'application/x-mimearchive',
    '.mhtml': 'application/x-mimearchive',
    '.mid': 'audio/midi',
    '.midi': 'audio/midi',
    '.mif': 'application/x-mif',
    '.minipsf': 'audio/x-minipsf',
    '.mk': 'text/x-makefile',
    '.mka': 'audio/x-matroska',
    '.mkd': 'text/x-markdown',
    '.mkv': 'video/x-matroska',
    '.ml': 'text/x-ocaml',
    '.mli': 'text/x-ocaml',
    '.mm': 'text/x-troff-mm',
    '.mmf': 'application/x-smaf',
    '.mml': 'application/mathml+xml',
    '.mng': 'video/x-mng',
    '.mo': 'text/x-modelica',
    '.mo3': 'audio/x-mo3',
    '.mobi': 'application/x-mobipocket-ebook',
    '.moc': 'text/x-moc',
    '.mod': 'audio/x-mod',
    '.mof': 'text/x-mof',
    '.moov': 'video/quicktime',
    '.mov': 'video/quicktime',
    '.movie': 'video/x-sgi-movie',
    '.mp+': 'audio/x-musepack',
    '.mp2': 'video/mpeg',
    '.mp3': 'audio/mpeg',
    '.mp4': 'video/mp4',
    '.mpc': 'audio/x-musepack',
    '.mpe': 'video/mpeg',
    '.mpeg': 'video/mpeg',
    '.mpg': 'video/mpeg',
    '.mpga': 'audio/mpeg',
    '.mpl': 'video/mp2t',
    '.mpls': 'video/mp2t',
    '.mpp': 'audio/x-musepack',
    '.mrl': 'text/x-mrml',
    '.mrml': 'text/x-mrml',
    '.mrw': 'image/x-minolta-mrw',
    '.ms': 'text/x-troff-ms',
    '.msi': 'application/x-msi',
    '.msod': 'image/x-msod',
    '.msx': 'application/x-msx-rom',
    '.mtm': 'audio/x-mod',
    '.mts': 'video/mp2t',
    '.mup': 'text/x-mup',
    '.mxf': 'application/mxf',
    '.mxu': 'video/vnd.mpegurl',
    '.n64': 'application/x-n64-rom',
    '.nb': 'application/mathematica',
    '.nc': 'application/x-netcdf',
    '.nds': 'application/x-nintendo-ds-rom',
    '.nef': 'image/x-nikon-nef',
    '.nes': 'application/x-nes-rom',
    '.nfo': 'text/x-nfo',
    '.not': 'text/x-mup',
    '.nsc': 'application/x-netshow-channel',
    '.nsv': 'video/x-nsv',
    '.nzb': 'application/x-nzb',
    '.o': 'application/x-object',
    '.obj': 'application/x-tgif',
    '.ocl': 'text/x-ocl',
    '.oda': 'application/oda',
    '.odb': 'application/vnd.oasis.opendocument.database',
    '.odc': 'application/vnd.oasis.opendocument.chart',
    '.odf': 'application/vnd.oasis.opendocument.formula',
    '.odg': 'application/vnd.oasis.opendocument.graphics',
    '.odi': 'application/vnd.oasis.opendocument.image',
    '.odm': 'application/vnd.oasis.opendocument.text-master',
    '.odp': 'application/vnd.oasis.opendocument.presentation',
    '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
    '.odt': 'application/vnd.oasis.opendocument.text',
    '.oga': 'audio/ogg',
    '.ogg': 'application/ogg',
    '.ogm': 'video/x-ogm+ogg',
    '.ogv': 'video/ogg',
    '.ogx': 'application/ogg',
    '.old': 'application/x-trash',
    '.oleo': 'application/x-oleo',
    '.ooc': 'text/x-ooc',
    '.opml': 'text/x-opml+xml',
    '.oprc': 'application/vnd.palm',
    '.ora': 'image/openraster',
    '.orf': 'image/x-olympus-orf',
    '.otc': 'application/vnd.oasis.opendocument.chart-template',
    '.otf': 'application/x-font-otf',
    '.otg': 'application/vnd.oasis.opendocument.graphics-template',
    '.oth': 'application/vnd.oasis.opendocument.text-web',
    '.otp': 'application/vnd.oasis.opendocument.presentation-template',
    '.ots': 'application/vnd.oasis.opendocument.spreadsheet-template',
    '.ott': 'application/vnd.oasis.opendocument.text-template',
    '.owl': 'application/rdf+xml',
    '.oxps': 'application/oxps',
    '.oxt': 'application/vnd.openofficeorg.extension',
    '.p': 'text/x-pascal',
    '.p10': 'application/pkcs10',
    '.p12': 'application/x-pkcs12',
    '.p7b': 'application/x-pkcs7-certificates',
    '.p7c': 'application/pkcs7-mime',
    '.p7m': 'application/pkcs7-mime',
    '.p7s': 'application/pkcs7-signature',
    '.p8': 'application/pkcs8',
    '.pack': 'application/x-java-pack200',
    '.pak': 'application/x-pak',
    '.par2': 'application/x-par2',
    '.pas': 'text/x-pascal',
    '.patch': 'text/x-patch',
    '.pbm': 'image/x-portable-bitmap',
    '.pcap': 'application/vnd.tcpdump.pcap',
    '.pcd': 'image/x-photo-cd',
    '.pcf': 'application/x-cisco-vpn-settings',
    '.pcf.gz': 'application/x-font-pcf',
    '.pcf.z': 'application/x-font-pcf',
    '.pcl': 'application/vnd.hp-pcl',
    '.pct': 'image/x-pict',
    '.pcx': 'image/x-pcx',
    '.pdb': 'chemical/x-pdb',
    '.pdc': 'application/x-aportisdoc',
    '.pdf': 'application/pdf',
    '.pdf.bz2': 'application/x-bzpdf',
    '.pdf.gz': 'application/x-gzpdf',
    '.pdf.xz': 'application/x-xzpdf',
    '.pef': 'image/x-pentax-pef',
    '.pem': 'application/x-x509-ca-cert',
    '.perl': 'application/x-perl',
    '.pfa': 'application/x-font-type1',
    '.pfb': 'application/x-font-type1',
    '.pfx': 'application/x-pkcs12',
    '.pgm': 'image/x-portable-graymap',
    '.pgn': 'application/x-chess-pgn',
    '.pgp': 'application/pgp-encrypted',
    '.php': 'application/x-php',
    '.php3': 'application/x-php',
    '.php4': 'application/x-php',
    '.php5': 'application/x-php',
    '.phps': 'application/x-php',
    '.pict': 'image/x-pict',
    '.pict1': 'image/x-pict',
    '.pict2': 'image/x-pict',
    '.pk': 'application/x-tex-pk',
    '.pkipath': 'application/pkix-pkipath',
    '.pkr': 'application/pgp-keys',
    '.pl': 'application/x-perl',
    '.pla': 'audio/x-iriver-pla',
    '.pln': 'application/x-planperfect',
    '.pls': 'audio/x-scpls',
    '.pm': 'application/x-perl',
    '.png': 'image/x-apple-ios-png',
    '.pnm': 'image/x-portable-anymap',
    '.pntg': 'image/x-macpaint',
    '.po': 'text/x-gettext-translation',
    '.por': 'application/x-spss-por',
    '.pot': 'text/x-gettext-translation-template',
    '.potm': 'application/vnd.ms-powerpoint.template.macroenabled.12',
    '.potx': 'application/vnd.openxmlformats-officedocument.presentationml.template',
    '.ppam': 'application/vnd.ms-powerpoint.addin.macroenabled.12',
    '.ppm': 'image/x-portable-pixmap',
    '.pps': 'application/vnd.ms-powerpoint',
    '.ppsm': 'application/vnd.ms-powerpoint.slideshow.macroenabled.12',
    '.ppsx': 'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
    '.ppt': 'application/vnd.ms-powerpoint',
    '.pptm': 'application/vnd.ms-powerpoint.presentation.macroenabled.12',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.ppz': 'application/vnd.ms-powerpoint',
    '.pqa': 'application/vnd.palm',
    '.prc': 'application/vnd.palm',
    '.ps': 'application/postscript',
    '.ps.bz2': 'application/x-bzpostscript',
    '.ps.gz': 'application/x-gzpostscript',
    '.psd': 'image/vnd.adobe.photoshop',
    '.psf': 'audio/x-psf',
    '.psf.gz': 'application/x-gz-font-linux-psf',
    '.psflib': 'audio/x-psflib',
    '.psid': 'audio/prs.sid',
    '.psw': 'application/x-pocket-word',
    '.pw': 'application/x-pw',
    '.py': 'text/x-python',
    '.pyc': 'application/x-python-bytecode',
    '.pickle': 'application/python-pickle',
    '.pyo': 'application/x-python-bytecode',
    '.qif': 'image/x-quicktime',
    '.qml': 'text/x-qml',
    '.qt': 'video/quicktime',
    '.qti': 'application/x-qtiplot',
    '.qti.gz': 'application/x-qtiplot',
    '.qtif': 'image/x-quicktime',
    '.qtl': 'application/x-quicktime-media-link',
    '.qtvr': 'video/quicktime',
    '.ra': 'audio/vnd.rn-realaudio',
    '.raf': 'image/x-fuji-raf',
    '.ram': 'application/ram',
    '.rar': 'application/x-rar',
    '.ras': 'image/x-cmu-raster',
    '.raw': 'image/x-panasonic-raw',
    '.rax': 'audio/vnd.rn-realaudio',
    '.rb': 'application/x-ruby',
    '.rdf': 'application/rdf+xml',
    '.rdfs': 'application/rdf+xml',
    '.reg': 'text/x-ms-regedit',
    '.rej': 'text/x-reject',
    '.rgb': 'image/x-rgb',
    '.rle': 'image/rle',
    '.rm': 'application/vnd.rn-realmedia',
    '.rmj': 'application/vnd.rn-realmedia',
    '.rmm': 'application/vnd.rn-realmedia',
    '.rms': 'application/vnd.rn-realmedia',
    '.rmvb': 'application/vnd.rn-realmedia',
    '.rmx': 'application/vnd.rn-realmedia',
    '.rnc': 'application/relax-ng-compact-syntax',
    '.rng': 'application/xml',
    '.roff': 'text/troff',
    '.rp': 'image/vnd.rn-realpix',
    '.rpm': 'application/x-rpm',
    '.rss': 'application/rss+xml',
    '.rt': 'text/vnd.rn-realtext',
    '.rtf': 'application/rtf',
    '.rtx': 'text/richtext',
    '.rv': 'video/vnd.rn-realvideo',
    '.rvx': 'video/vnd.rn-realvideo',
    '.rw2': 'image/x-panasonic-raw2',
    '.s3m': 'audio/x-s3m',
    '.sam': 'application/x-amipro',
    '.sami': 'application/x-sami',
    '.sav': 'application/x-spss-sav',
    '.scala': 'text/x-scala',
    '.scm': 'text/x-scheme',
    '.sda': 'application/vnd.stardivision.draw',
    '.sdc': 'application/vnd.stardivision.calc',
    '.sdd': 'application/vnd.stardivision.impress',
    '.sdp': 'application/sdp',
    '.sds': 'application/vnd.stardivision.chart',
    '.sdw': 'application/vnd.stardivision.writer',
    '.sgf': 'application/x-go-sgf',
    '.sgi': 'image/x-sgi',
    '.sgl': 'application/vnd.stardivision.writer',
    '.sgm': 'text/sgml',
    '.sgml': 'text/sgml',
    '.sh': 'application/x-shellscript',
    '.shape': 'application/x-dia-shape',
    '.shar': 'application/x-shar',
    '.shn': 'application/x-shorten',
    '.siag': 'application/x-siag',
    '.sid': 'audio/prs.sid',
    '.sik': 'application/x-trash',
    '.sis': 'application/vnd.symbian.install',
    '.sisx': 'x-epoc/x-sisx-app',
    '.sit': 'application/x-stuffit',
    '.siv': 'application/sieve',
    '.sk': 'image/x-skencil',
    '.sk1': 'image/x-skencil',
    '.skr': 'application/pgp-keys',
    '.sldm': 'application/vnd.ms-powerpoint.slide.macroenabled.12',
    '.sldx': 'application/vnd.openxmlformats-officedocument.presentationml.slide',
    '.slk': 'text/spreadsheet',
    '.smaf': 'application/x-smaf',
    '.smc': 'application/x-snes-rom',
    '.smd': 'application/vnd.stardivision.mail',
    '.smf': 'application/vnd.stardivision.math',
    '.smi': 'application/x-sami',
    '.smil': 'application/smil',
    '.sml': 'application/smil',
    '.sms': 'application/x-sms-rom',
    '.snd': 'audio/basic',
    '.so': 'application/x-sharedlib',
    '.spc': 'application/x-pkcs7-certificates',
    '.spd': 'application/x-font-speedo',
    '.spec': 'text/x-rpm-spec',
    '.spl': 'application/x-shockwave-flash',
    '.spm': 'application/x-source-rpm',
    '.spx': 'audio/x-speex',
    '.sql': 'text/x-sql',
    '.sr2': 'image/x-sony-sr2',
    '.src': 'application/x-wais-source',
    '.src.rpm': 'application/x-source-rpm',
    '.srf': 'image/x-sony-srf',
    '.srt': 'application/x-subrip',
    '.ss': 'text/x-scheme',
    '.ssa': 'text/x-ssa',
    '.stc': 'application/vnd.sun.xml.calc.template',
    '.std': 'application/vnd.sun.xml.draw.template',
    '.sti': 'application/vnd.sun.xml.impress.template',
    '.stm': 'audio/x-stm',
    '.stw': 'application/vnd.sun.xml.writer.template',
    '.sty': 'text/x-tex',
    '.sub': 'text/x-subviewer',
    '.sun': 'image/x-sun-raster',
    '.sv': 'text/x-svsrc',
    '.sv4cpio': 'application/x-sv4cpio',
    '.sv4crc': 'application/x-sv4crc',
    '.svg': 'image/svg+xml',
    '.svgz': 'image/svg+xml-compressed',
    '.svh': 'text/x-svhdr',
    '.swf': 'application/x-shockwave-flash',
    '.swm': 'application/x-ms-wim',
    '.sxc': 'application/vnd.sun.xml.calc',
    '.sxd': 'application/vnd.sun.xml.draw',
    '.sxg': 'application/vnd.sun.xml.writer.global',
    '.sxi': 'application/vnd.sun.xml.impress',
    '.sxm': 'application/vnd.sun.xml.math',
    '.sxw': 'application/vnd.sun.xml.writer',
    '.sylk': 'text/spreadsheet',
    '.t': 'text/troff',
    '.t2t': 'text/x-txt2tags',
    '.tar': 'application/x-tar',
    '.tar.bz': 'application/x-bzip-compressed-tar',
    '.tar.bz2': 'application/x-bzip-compressed-tar',
    '.tar.gz': 'application/x-compressed-tar',
    '.tar.lrz': 'application/x-lrzip-compressed-tar',
    '.tar.lzma': 'application/x-lzma-compressed-tar',
    '.tar.lzo': 'application/x-tzo',
    '.tar.xz': 'application/x-xz-compressed-tar',
    '.tar.z': 'application/x-tarz',
    '.taz': 'application/x-tarz',
    '.tb2': 'application/x-bzip-compressed-tar',
    '.tbz': 'application/x-bzip-compressed-tar',
    '.tbz2': 'application/x-bzip-compressed-tar',
    '.tcl': 'text/x-tcl',
    '.tex': 'text/x-tex',
    '.texi': 'text/x-texinfo',
    '.texinfo': 'text/x-texinfo',
    '.tga': 'image/x-tga',
    '.tgz': 'application/x-compressed-tar',
    '.theme': 'application/x-theme',
    '.themepack': 'application/x-windows-themepack',
    '.tif': 'image/tiff',
    '.tiff': 'image/tiff',
    '.tk': 'text/x-tcl',
    '.tlrz': 'application/x-lrzip-compressed-tar',
    '.tlz': 'application/x-lzma-compressed-tar',
    '.tnef': 'application/vnd.ms-tnef',
    '.tnf': 'application/vnd.ms-tnef',
    '.toc': 'application/x-cdrdao-toc',
    '.torrent': 'application/x-bittorrent',
    '.tpic': 'image/x-tga',
    '.tr': 'text/troff',
    '.ts': 'video/mp2t',
    '.tsv': 'text/tab-separated-values',
    '.tta': 'audio/x-tta',
    '.ttc': 'application/x-font-ttf',
    '.ttf': 'application/x-font-ttf',
    '.ttx': 'application/x-font-ttx',
    '.txt': 'text/plain',
    '.txz': 'application/x-xz-compressed-tar',
    '.tzo': 'application/x-tzo',
    '.ufraw': 'application/x-ufraw',
    '.ui': 'application/x-gtk-builder',
    '.uil': 'text/x-uil',
    '.ult': 'audio/x-mod',
    '.uni': 'audio/x-mod',
    '.url': 'application/x-mswinurl',
    '.ustar': 'application/x-ustar',
    '.uue': 'text/x-uuencode',
    '.v': 'text/x-verilog',
    '.vala': 'text/x-vala',
    '.vapi': 'text/x-vala',
    '.vcard': 'text/vcard',
    '.vcf': 'text/vcard',
    '.vcs': 'text/calendar',
    '.vct': 'text/vcard',
    '.vda': 'image/x-tga',
    '.vhd': 'text/x-vhdl',
    '.vhdl': 'text/x-vhdl',
    '.viv': 'video/vivo',
    '.vivo': 'video/vivo',
    '.vlc': 'audio/x-mpegurl',
    '.vob': 'video/mpeg',
    '.voc': 'audio/x-voc',
    '.vor': 'application/vnd.stardivision.writer',
    '.vrm': 'model/vrml',
    '.vrml': 'model/vrml',
    '.vsd': 'application/vnd.visio',
    '.vss': 'application/vnd.visio',
    '.vst': 'image/x-tga',
    '.vsw': 'application/vnd.visio',
    '.vtt': 'text/vtt',
    '.w2p': 'application/w2p',
    '.wav': 'audio/x-wav',
    '.wax': 'audio/x-ms-asx',
    '.wb1': 'application/x-quattropro',
    '.wb2': 'application/x-quattropro',
    '.wb3': 'application/x-quattropro',
    '.wbmp': 'image/vnd.wap.wbmp',
    '.wcm': 'application/vnd.ms-works',
    '.wdb': 'application/vnd.ms-works',
    '.webm': 'video/webm',
    '.wim': 'application/x-ms-wim',
    '.wk1': 'application/vnd.lotus-1-2-3',
    '.wk3': 'application/vnd.lotus-1-2-3',
    '.wk4': 'application/vnd.lotus-1-2-3',
    '.wks': 'application/vnd.ms-works',
    '.wma': 'audio/x-ms-wma',
    '.wmf': 'image/x-wmf',
    '.wml': 'text/vnd.wap.wml',
    '.wmls': 'text/vnd.wap.wmlscript',
    '.wmv': 'video/x-ms-wmv',
    '.wmx': 'audio/x-ms-asx',
    '.woff': 'application/font-woff',
    '.wp': 'application/vnd.wordperfect',
    '.wp4': 'application/vnd.wordperfect',
    '.wp5': 'application/vnd.wordperfect',
    '.wp6': 'application/vnd.wordperfect',
    '.wpd': 'application/vnd.wordperfect',
    '.wpg': 'application/x-wpg',
    '.wpl': 'application/vnd.ms-wpl',
    '.wpp': 'application/vnd.wordperfect',
    '.wps': 'application/vnd.ms-works',
    '.wri': 'application/x-mswrite',
    '.wrl': 'model/vrml',
    '.wsgi': 'text/x-python',
    '.wv': 'audio/x-wavpack',
    '.wvc': 'audio/x-wavpack-correction',
    '.wvp': 'audio/x-wavpack',
    '.wvx': 'audio/x-ms-asx',
    '.wwf': 'application/x-wwf',
    '.x3f': 'image/x-sigma-x3f',
    '.xac': 'application/x-gnucash',
    '.xbel': 'application/x-xbel',
    '.xbl': 'application/xml',
    '.xbm': 'image/x-xbitmap',
    '.xcf': 'image/x-xcf',
    '.xcf.bz2': 'image/x-compressed-xcf',
    '.xcf.gz': 'image/x-compressed-xcf',
    '.xhtml': 'application/xhtml+xml',
    '.xi': 'audio/x-xi',
    '.xla': 'application/vnd.ms-excel',
    '.xlam': 'application/vnd.ms-excel.addin.macroenabled.12',
    '.xlc': 'application/vnd.ms-excel',
    '.xld': 'application/vnd.ms-excel',
    '.xlf': 'application/x-xliff',
    '.xliff': 'application/x-xliff',
    '.xll': 'application/vnd.ms-excel',
    '.xlm': 'application/vnd.ms-excel',
    '.xlr': 'application/vnd.ms-works',
    '.xls': 'application/vnd.ms-excel',
    '.xlsb': 'application/vnd.ms-excel.sheet.binary.macroenabled.12',
    '.xlsm': 'application/vnd.ms-excel.sheet.macroenabled.12',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.xlt': 'application/vnd.ms-excel',
    '.xltm': 'application/vnd.ms-excel.template.macroenabled.12',
    '.xltx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
    '.xlw': 'application/vnd.ms-excel',
    '.xm': 'audio/x-xm',
    '.xmf': 'audio/x-xmf',
    '.xmi': 'text/x-xmi',
    '.xml': 'application/xml',
    '.xpi': 'application/x-xpinstall',
    '.xpm': 'image/x-xpixmap',
    '.xps': 'application/oxps',
    '.xsd': 'application/xml',
    '.xsl': 'application/xslt+xml',
    '.xslfo': 'text/x-xslfo',
    '.xslt': 'application/xslt+xml',
    '.xspf': 'application/xspf+xml',
    '.xul': 'application/vnd.mozilla.xul+xml',
    '.xwd': 'image/x-xwindowdump',
    '.xyz': 'chemical/x-pdb',
    '.xz': 'application/x-xz',
    '.yaml': 'application/x-yaml',
    '.yml': 'application/x-yaml',
    '.z': 'application/x-compress',
    '.zabw': 'application/x-abiword',
    '.zip': 'application/zip',
    '.zoo': 'application/x-zoo',
}


def contenttype(filename, default='text/plain'):
    """
    Returns the Content-Type string matching extension of the given filename.
    """

    i = filename.rfind('.')
    if i >= 0:
        default = CONTENT_TYPE.get(filename[i:].lower(), default)
        j = filename.rfind('.', 0, i)
        if j >= 0:
            default = CONTENT_TYPE.get(filename[j:].lower(), default)
    if default.startswith('text/'):
        default += '; charset=utf-8'
    return default
