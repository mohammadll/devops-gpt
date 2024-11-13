

def IaC_template_generator_docker(input) -> str:

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions resources for {input.base_config} ensuring a modular, flexible structure
              to enable users to configure all essential settings at the root level. Only provide Python code,
              no explanations or markdown formatting. The project should be organized as follows:
              1. Root Directory Structure:
                  - main.tf:
                      - Contains a provider block, configured with flexible variables where required to allow
                        users to specify provider settings without hardcoding.
                      - Defines a module block that references {input.base_config} from a subdirectory within
                        modules. This module block should expose all variables that {input.base_config} requires,
                        allowing configuration at the root level rather than directly within the module.
                      - Every variable defined in {input.base_config} should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {input.base_config} by
                        modifying root main.tf.
                  - variables.tf:
                      - Declares all variables that users might need to configure for {input.base_config}.
                        These should include any inputs required by the provider or the {input.base_config}
                        resource, as well as optional parameters that users may want to customize.
                      - Variable descriptions should clearly indicate their purpose, and default values should
                        be avoided unless there are reasonable, common defaults, to maintain flexibility and
                        encourage explicit configuration.
                      - All types of variables can be used such as (number, string, bool, list(string),
                        map(string), list(map(string)), map(map(string)), object(), any)
                  - terraform.tfvars:
                      - Provides default values for variables declared in the root `variables.tf`, making it easy
                        for users to define common configurations.
                      - This file should be structured to include any typical default settings without hardcoding
                        sensitive values.
                  - versions.tf:
                      - Contains the `terraform` and `provider` blocks, specifying required versions.

                      - If {input.base_config} is a Docker resource, set kreuzwerker/docker as the provider with appropriate version constraints.
                      - If {input.base_config} is an AWS resource, set hashicorp/aws as the provider with suitable version constraints.

                      - Structure the `terraform` block as:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                <provider_name> = {{
                                  source  = "<source>"
                                  version = ">= <version>"
                               }}
                              }}
                            }}
                  - outputs.tf:
                      - Exposes relevant outputs from {input.base_config}, retrieving them from the module output
                        and making them accessible at the root level. Each output should have a clear description,
                        making it easy for users to understand the value and purpose of the output data.
              2. Module Directory Structure (modules/{input.base_config}):
                  - main.tf:
                      - Defines the {input.base_config} resource, fully utilizing required and also some optional
                        parameters. Avoid any hardcoded values within the module to support full configurability
                        from the root level.
                      - Required parameters should cover the essentials for creating {input.base_config}, while
                        optional parameters should provide a range of additional settings that enable more
                        granular configuration if desired.
                  - variables.tf:
                      - Lists all variables necessary for configuring {input.base_config}, with descriptions and
                        types specified to improve usability. No default values should be set here unless
                        necessary for required fields.
                      - Variable names should be clear and consistent with naming conventions in the root
                        variables file, ensuring consistency in usage.
                  - terraform.tfvars:
                      - Includes default values for module-level variables to ensure that common parameters have
                        defaults. This `terraform.tfvars` file within the module should be structured to provide
                        typical configuration values, making it easier to set up and reducing the need for hardcoded values.
                  - versions.tf:
                      - Contains the `terraform` and `provider` blocks, specifying required versions.
                      - If {input.base_config} is a Docker resource, set kreuzwerker/docker as the provider with appropriate version constraints.
                      - If {input.base_config} is an AWS resource, set hashicorp/aws as the provider with suitable version constraints.

                      - Structure the `terraform` block as:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                <provider_name> = {{
                                  source  = "<source>"
                                  version = ">= <version>"
                                }}
                              }}
                            }}
                  - outputs.tf:
                      - Specifies outputs for the {input.base_config} resource, selecting relevant data that users
                        might need to access from the root level. Each output should have an informative
                        description, so users can understand its purpose and utility.
              Ensure this project structure supports {input.base_config}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

                import os
                project_name = "app/media/MyTerraform"
                moduels_dir = os.path.join(project_name, "modules")

                # Create project directories

                os.makedirs(moduels_dir, exist_ok=True)

                # Create main.tf (for example)
                with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                    # any thing you need



            """
    return prompt