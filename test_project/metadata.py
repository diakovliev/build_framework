
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
    }
