
def get_metadata():
    return {
        "properties" : {
            "project"   : "Test project",
            "version"   : "0.0.1",
            "user"      : metadata.GetEnv("USER"),
            "home"      : metadata.GetEnv("HOME"),
            "file1"     : metadata.ReadFile("file1"),
            "file2"     : metadata.ReadFile("file2"),
        },
        "components": {
            "first_component_id": {
                "properties": {
                    "name": "First component",
                },
                "repositories": {
                    "repo1": metadata.GitInfo("repos/repo1"),
                    "repo2": metadata.GitInfo("repos/repo2"),
                },
            },
            "second_component_id": {
                "properties": {
                    "name": "Second component",
                },
                "repositories": {
                    "repo3": metadata.GitInfo("repos/repo3"),
                    "repo4": metadata.GitInfo("repos/repo4"),
                },
            }
        },
    }
