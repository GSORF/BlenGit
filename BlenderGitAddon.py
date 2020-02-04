bl_info = {
    "name": "BlenGit",
    "description": "A Blender Addon for helping in using git version control.",
    "author": "Cutyno, BlenderEi",
    "version": (1, 0),
    "blender": (2, 8, 3),
    "location": "View3D > Tools > BlenGit",
    "warning": "Work in Progress!", # used for warning icon and text in addons panel
    "wiki_url": "https://github.com/GSORF/BlenderGitAddon",
    "tracker_url": "https://github.com/GSORF/BlenderGitAddon",
    "support": "COMMUNITY",
    "category": "Import-Export"
}



'''
###############################
Currently Work in Progress Code - do not use!
###############################
'''







'''
###############################
Example for Batch Export:
###############################
'''

'''
# exports each selected object into its own file

import bpy
import os

# export to blend file location
basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

view_layer = bpy.context.view_layer

obj_active = view_layer.objects.active
selection = bpy.context.selected_objects

bpy.ops.object.select_all(action='DESELECT')

for obj in selection:

    obj.select_set(True)

    # some exporters only use the active object
    view_layer.objects.active = obj

    name = bpy.path.clean_name(obj.name)
    fn = os.path.join(basedir, name)

    bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)

    # Can be used for multiple formats
    # bpy.ops.export_scene.x3d(filepath=fn + ".x3d", use_selection=True)

    obj.select_set(False)

    print("written:", fn)


view_layer.objects.active = obj_active

for obj in selection:
    obj.select_set(True)
'''





'''
###############################
Example for Blender Addon:
###############################
'''

import bpy



class BlenderGitAddon(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context_mode = 'OBJECT'
    bl_category = "BlendGit"

    bl_idname = "VIEW3D_PT_BlenderGitAddonPanel"
    bl_label = "BlendGit Addon"
    bl_description = (
        "This is a addon\n"
        "written for use with git"
    )
    '''
    bl_icon = "ops.generic.select_lasso"
    bl_widget = None
    bl_keymap = (
        ("view3d.select_lasso", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
        ("view3d.select_lasso", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
         {"properties": [("mode", 'SUB')]}),
    )
    '''
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        layout.label(text=" Simple Row:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create an row where the buttons are aligned to each other.
        layout.label(text=" Aligned Row:")

        row = layout.row(align=True)
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.label(text="Column One:")
        col.prop(scene, "frame_end")
        col.prop(scene, "frame_start")

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Column Two:")
        col.prop(scene, "frame_start")
        col.prop(scene, "frame_end")

        # Big render button
        layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("render.render")
        row.operator("render.render", text="My custom Text", text_ctxt="", translate=True, icon='TRASH', emboss=True, depress=False, icon_value=0)

        # Different sizes in a row
        layout.label(text="Different button sizes:")
        row = layout.row(align=True)
        row.operator("render.render")

        sub = row.row()
        sub.scale_x = 2.0
        sub.operator("render.render")

        row.operator("render.render")


def register():
    bpy.utils.register_class(BlenderGitAddon)
    

def unregister():
    bpy.utils.unregister_class(BlenderGitAddon)


if __name__ == "__main__":
    register()