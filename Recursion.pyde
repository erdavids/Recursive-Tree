w, h = 1000, 1000

length_depr = .5
max_depth = 11
min_length = 30

def draw_line(p, v, l, d, md):
    if (d > md):
        return
    
    if (l < min_length):
        l = min_length
    
    
    start_point = p
    end_point = (p[0] + v[0] * l, p[1] + v[1] * l)
    
    #line(start_point[0], start_point[1], end_point[0], end_point[1])
    strokeWeight(4 - d/3)
    lr = -40
    hr = 40
    curve(start_point[0] + random(lr, hr), start_point[1] + random(lr, hr), start_point[0], start_point[1], end_point[0], end_point[1], end_point[0] + random(lr, hr), end_point[1] + random(lr, hr))
    
    v_one = v.copy()
    v_one.rotate(random(.1, .35) * PI)
    draw_line(end_point, v_one, l * length_depr, d + 1, md)
    
    v_two = v.copy()
    v_two.rotate(random(1.65, 1.85) * PI)
    draw_line(end_point, v_two, l * length_depr, d + 1, md)
    
    
              
def setup():
    size(w, h)
    pixelDensity(2)
    
    background(220, 245, 245)
    stroke(0)
    strokeWeight(1)
    noFill()
    
    fill(255)
    noStroke()
    for i in range(20):
        rect(0, i * 60, w, 10)
    
    stroke(0)
    strokeWeight(1)
    noFill()
    v = PVector(0.0, -1.0)
    draw_line((w/2, h), v, h/3, 0, 10)
    

    noStroke()
    fill(255)
    for i in range(20):
        rect(0, i * 60 + 30, w, 10)
    
    save("Examples/ex.jpg")
    

    
    
