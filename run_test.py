"""
Run start for FactoryGame test suite.
"""

import sys

try:
    # Py 3.6
    py_36_path, _ = sys.argv[0].split("/")
except ValueError:
    # Py 3.2
    sys.path.insert(0, "\\".join(sys.argv[0].split("\\")[:-1]))
else:
    sys.path.insert(0, py_36_path)

## Whether to run GUI tests.
RUN_GUI_TESTS = "nogui" not in sys.argv


if __name__ != "__main__":
    exit(1)

if RUN_GUI_TESTS:
    # Create gui_test_manager object for root window.
    from test.template.template_gui import GuiTestManager
    gui_test_manager = GuiTestManager()
    
    # Add test for tkutils.
    from test.utils.tkutils_test import MotionInputTest, ScalingImageTest
    gui_test_manager.add_test(MotionInputTest)
    gui_test_manager.add_test(ScalingImageTest)

    # Add test for blueprints.
    from test.core.blueprint_test import GraphMotionTest, GraphResizeTest
    gui_test_manager.add_test(GraphMotionTest)
    gui_test_manager.add_test(GraphResizeTest)

    # Add test for engine.
    from test.core.engine_test import EngineTickTest
    gui_test_manager.add_test(EngineTickTest)

    # Start mainloop.
    gui_test_manager.mainloop()
