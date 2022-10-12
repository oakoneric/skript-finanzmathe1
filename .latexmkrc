@default_files = ('stochv_vorlesung_main.tex');

$pdf_mode = 1;

$dvi_previewer = 'start xdvi -watchfile 1.5';
$ps_previewer  = 'start gv --watch';
$pdf_previewer = 'start evince %S';

$clean_ext = "bbl dvi ps gz thm nav out snm";
