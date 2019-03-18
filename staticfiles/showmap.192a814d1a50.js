map = new OpenLayers.Map("map");
map.addLayer(new OpenLayers.Layer.OSM());
map.zoomToMaxExtent();

var layer = new OpenLayers.Layer.GML("GML", "{% url gml/torrenti.gml %}")
map.addLayer(layer);
