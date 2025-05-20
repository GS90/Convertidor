application_id = 'tech.digiroad.Convertidor'

scalable_dir = 'hicolor' / 'scalable' / 'apps'
install_data(
  scalable_dir / ('@0@.svg').format(application_id),
  install_dir: get_option('datadir') / 'icons' / scalable_dir
)

symbolic_dir = 'hicolor' / 'symbolic' / 'apps'
install_data(
  symbolic_dir / ('@0@-symbolic.svg').format(application_id),

  symbolic_dir / 'actions' / ('copy-symbolic.svg'),
  symbolic_dir / 'actions' / ('minus-symbolic.svg'),
  symbolic_dir / 'actions' / ('plus-symbolic.svg'),

  symbolic_dir / 'quantities' / ('q-angle-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-area-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-digital-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-energy-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-force-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-fuel-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-length-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-mass-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-numbers-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-power-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-pressure-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-speed-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-temperature-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-time-symbolic.svg'),
  symbolic_dir / 'quantities' / ('q-volume-symbolic.svg'),

  install_dir: get_option('datadir') / 'icons' / symbolic_dir
)