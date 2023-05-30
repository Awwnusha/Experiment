def update_sprite(self):
        sprite_sheet ="idle"
        if self.x_val != 0: #ratish
            sprite_sheet ="run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update_sprite()
        