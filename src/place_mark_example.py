import simplekml


def place_mark_example():
    kml = simplekml.Kml()
    kml.document.name = "Test"
    # longitude, latitude, altitude (optional)
    kml.newpoint(name="Hercilio Luz Bridge", description="Bridge in Florianopolis",
                 coords=[(-48.565198, -27.593734, 0)])
    kml.save('test_marker.kml')
