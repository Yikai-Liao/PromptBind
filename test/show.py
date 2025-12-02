import prelude

from example import example_function, ExampleClass
from promptbind.util import get_prompt_key, set_prompt_key_patch, unset_prompt_key_patch

if __name__ == "__main__":
    print("Prompt key for example_function:", get_prompt_key(example_function))
    set_prompt_key_patch(example_function, "patched_key_for_example_function")
    example_function()
    unset_prompt_key_patch(example_function)
    example_function()
    obj = ExampleClass()
    obj.class_method()