import simplekml


def path_example():
    kml = simplekml.Kml()
    kml.newpoint(name="A", coords=[(-48.544988, -27.583643, 0)])  # lon, lat optional height
    kml.newpoint(name="B", coords=[(-48.543507, -27.585887, 0)])  # lon, lat optional height

    line_string = kml.newlinestring(name='A Path', extrude=1, altitudemode=simplekml.AltitudeMode.relativetoground)
    line_string.coords = [(-48.544988, -27.583643, 0), (-48.543507, -27.585887, 0)]

    # add style
    line_string.style.linestyle.width = 5
    line_string.style.linestyle.color = simplekml.Color.blue

    kml.save('test_path.kml')