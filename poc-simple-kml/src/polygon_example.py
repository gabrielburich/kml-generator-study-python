import simplekml


def polygon_example():
    kml = simplekml.Kml()
    polyline = kml.newpolygon(name='Building', extrude=1, altitudemode=simplekml.AltitudeMode.relativetoground)

    polyline.outerboundaryis = [
        (-48.543789, -27.590048, 60),
        (-48.543474, -27.590053, 60),
        (-48.543482, -27.590357, 60),
        (-48.543785, -27.590314, 60)
    ]
    kml.save("test_polygon.kml")
