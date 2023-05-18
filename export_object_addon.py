bl_info = {
    "name": "Export Object as FBX, OBJ, STL, and GLB",
    "author": "ahmudz",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "File > Export",
    "description": "Exports the selected object as FBX, OBJ, STL, and GLB files",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export"
}

import bpy
import os
from datetime import datetime

class ExportObject(bpy.types.Operator):
    """Export the selected object as FBX, OBJ, STL, and GLB files"""
    bl_idname = "export_object.export"
    bl_label = "Export Object as FBX, OBJ, STL, and GLB"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # Set the base path for the exported files
        base_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Create a new folder with the current date and time
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = os.path.join(base_path, now)
        os.makedirs(folder_path, exist_ok=True)

        # Get the name of the active object in Blender
        active_obj = bpy.context.view_layer.objects.active
        if active_obj is not None:
            file_name = active_obj.name
        else:
            file_name = "exported_object"

        # Export as FBX
        fbx_path = os.path.join(folder_path, file_name + ".fbx")
        bpy.ops.export_scene.fbx(filepath=fbx_path, use_selection=True)

        # Export as OBJ
        obj_path = os.path.join(folder_path, file_name + ".obj")
        bpy.ops.export_scene.obj(filepath=obj_path, use_selection=True)

        # Export as STL
        stl_path = os.path.join(folder_path, file_name + ".stl")
        bpy.ops.export_mesh.stl(filepath=stl_path, use_selection=True)

        # Export as GLB
        glb_path = os.path.join(folder_path, file_name + ".glb")
        bpy.ops.export_scene.gltf(filepath=glb_path, export_format='GLB', use_selection=True)

        return {'FINISHED'}

def menu_func_export(self, context):
    self.layout.operator(ExportObject.bl_idname, text="FBX, OBJ, STL, and GLB (.fbx, .obj, .stl, .glb)")

def register():
    bpy.utils.register_class(ExportObject)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportObject)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
