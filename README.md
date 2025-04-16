maybe guide soon

physics_tiles in engine/pygpen/tiles/tilemap.py

 assets
self.e['Assets'].load_folder('data/images/ASSET_NAME', colorkey=(0, 0, 0))

 tilemap
self.tilemap = pp.Tilemap(tile_size=TILE_SIZE)
self.tilemap.load('data/dbs/MAP/NAME.pmap', spawn_hook=gen_hook())

 tilemap render
visible_rect = pygame.Rect(
    self.camera[0] - 16, 
    self.camera[1] - 16,
    self.display.get_width() + 32, 
    self.display.get_height() + 32
)

self.tilemap.renderz(visible_rect, offset=self.camera)

 entitys
self.entity
self.e["EntityGroups"].add(self.entity, 'entities_group')