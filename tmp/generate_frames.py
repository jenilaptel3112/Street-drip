#!/usr/bin/env python3
import math

def generate_svg(t, width=720, height=960):
    """
    t ranges from 0.0 to 1.0 (animation progress)
    t = 0.0: head looking up (chin up, sunglasses high, underside of jaw prominent)
    t = 0.5: head looking straight
    t = 1.0: head tilted down (looking down intently, brow lowered, hair forward)
    """
    # Use smooth cosine curve for smooth head nod
    # pitch: -1.0 (looking up) to +1.0 (looking down)
    pitch = -math.cos(t * math.pi * 2)  # cycles -1 to 1 and back
    
    # Offsets based on pitch:
    # When pitch is -1 (up): face features shift up, chin stretches, neck visible, sunglasses higher
    # When pitch is +1 (down): forehead comes forward, sunglasses shift down, chin tucks in
    head_y = 480 + pitch * 35
    head_tilt = pitch * 12 # degrees
    
    # Feature vertical shifts:
    sunglasses_y = 420 + pitch * 45
    chin_y = 660 + pitch * 15
    tattoo_y = sunglasses_y + 80 + pitch * 10
    hair_crown_y = 260 + pitch * 20
    
    # Sunglasses reflection shift:
    refl_y = 5 - pitch * 18
    refl_opacity = 0.85 + pitch * 0.15
    
    # Ambient purple bounce intensity
    chin_glow_r = 180 + pitch * 40
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Background Gradient: Deep moody violet purple -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#190637" />
      <stop offset="45%" stop-color="#320f66" />
      <stop offset="75%" stop-color="#270950" />
      <stop offset="100%" stop-color="#14032a" />
    </linearGradient>

    <!-- Purple ambient bounce light on skin -->
    <radialGradient id="purpleBounce" cx="50%" cy="100%" r="60%">
      <stop offset="0%" stop-color="#a84bf0" stop-opacity="0.65" />
      <stop offset="40%" stop-color="#691ab3" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <!-- Face skin tones -->
    <radialGradient id="skinGrad" cx="45%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#ffe4d4" />
      <stop offset="35%" stop-color="#f8cbb0" />
      <stop offset="75%" stop-color="#e29e7c" />
      <stop offset="100%" stop-color="#8d4a77" />
    </radialGradient>

    <!-- Neck skin shading -->
    <linearGradient id="neckGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4f1852" />
      <stop offset="60%" stop-color="#87436b" />
      <stop offset="100%" stop-color="#e09b78" />
    </linearGradient>

    <!-- Hair Teal/Petrol base gradient -->
    <linearGradient id="hairDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#091b1a" />
      <stop offset="40%" stop-color="#123533" />
      <stop offset="80%" stop-color="#0a1e1d" />
      <stop offset="100%" stop-color="#050e0e" />
    </linearGradient>

    <!-- Hair lock specular cyan glow -->
    <radialGradient id="cyanHighlight" cx="50%" cy="30%" r="45%">
      <stop offset="0%" stop-color="#45fff0" stop-opacity="0.85" />
      <stop offset="40%" stop-color="#1eb5a7" stop-opacity="0.45" />
      <stop offset="85%" stop-color="#0f4540" stop-opacity="0" />
    </radialGradient>

    <!-- Sunglasses Frame Gloss -->
    <linearGradient id="frameGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#32333b" />
      <stop offset="40%" stop-color="#151619" />
      <stop offset="80%" stop-color="#09090b" />
      <stop offset="100%" stop-color="#1a1b22" />
    </linearGradient>

    <!-- Sunglasses Lens Gradient -->
    <radialGradient id="lensGrad" cx="50%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#24252f" />
      <stop offset="60%" stop-color="#0e0f13" />
      <stop offset="100%" stop-color="#050508" />
    </radialGradient>

    <!-- Lens Specular Reflection Softbox -->
    <linearGradient id="lensRefl" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="{0.75 * refl_opacity:.2f}" />
      <stop offset="35%" stop-color="#d9e6f2" stop-opacity="{0.35 * refl_opacity:.2f}" />
      <stop offset="80%" stop-color="#8ba1b8" stop-opacity="0" />
    </linearGradient>

    <!-- Drop Shadow filter -->
    <filter id="shadowFilter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Deep Purple Canvas -->
  <rect width="{width}" height="{height}" fill="url(#bgGrad)" />

  <!-- Four-point star sparkle in bottom right (from original video) -->
  <g transform="translate(605, 875) scale(1.1)" opacity="0.85">
    <!-- Center glow -->
    <circle cx="0" cy="0" r="4" fill="#d8b4fe" />
    <!-- 4 Diamond star points -->
    <path d="M 0 -22 Q 0 -5 18 0 Q 0 5 0 22 Q 0 5 -18 0 Q 0 -5 0 -22 Z" fill="#eeddfb" />
    <circle cx="0" cy="0" r="1.5" fill="#ffffff" />
  </g>

  <!-- Ambient background glow behind head -->
  <circle cx="360" cy="460" r="280" fill="#4d1685" opacity="0.35" filter="url(#shadowFilter)" />

  <!-- MAIN CHARACTER GROUP with 3D Head Tilt / Rotation -->
  <g transform="translate(360, {head_y}) rotate({head_tilt}) translate(-360, -{head_y})">
    
    <!-- Neck / Throat -->
    <path d="M 285 580 C 275 670, 270 780, 260 900 L 460 900 C 450 780, 445 670, 435 580 Z" fill="url(#neckGrad)" />
    <!-- Ambient purple bounce shadow under jaw -->
    <ellipse cx="360" cy="620" rx="110" ry="50" fill="#2d0a3d" opacity="0.8" />

    <!-- Left Ear (viewer's left is character's right, viewer's right is character's left) -->
    <!-- Character's right ear (viewer left) -->
    <g transform="translate(195, 480)">
      <ellipse cx="0" cy="0" rx="26" ry="42" fill="#e09e7c" transform="rotate(-8)" />
      <ellipse cx="4" cy="2" rx="14" ry="24" fill="#a85369" opacity="0.8" />
      <!-- Silver huggie ear cuffs -->
      <rect x="-14" y="-24" width="7" height="12" rx="3" fill="#cfd3db" stroke="#111" stroke-width="1.5" />
      <rect x="-15" y="-6" width="7" height="12" rx="3" fill="#cfd3db" stroke="#111" stroke-width="1.5" />
      <!-- Spike piercing -->
      <polygon points="-12,18 -18,34 -9,22" fill="#e2e5eb" stroke="#111" stroke-width="1.5" />
    </g>

    <!-- Character's left ear (viewer right) -->
    <g transform="translate(535, 495)">
      <ellipse cx="0" cy="0" rx="26" ry="44" fill="#d99373" transform="rotate(10)" />
      <ellipse cx="-4" cy="2" rx="14" ry="26" fill="#8f405c" opacity="0.85" />
      <!-- Silver huggie ear cuffs -->
      <rect x="8" y="-22" width="7" height="12" rx="3" fill="#cfd3db" stroke="#111" stroke-width="1.5" />
      <rect x="9" y="-4" width="7" height="12" rx="3" fill="#cfd3db" stroke="#111" stroke-width="1.5" />
      <!-- Dangling cross earring -->
      <g transform="translate(6, 28)">
        <circle cx="0" cy="0" r="3" fill="#ffffff" stroke="#111" stroke-width="1" />
        <path d="M 0 3 L 0 28 M -8 11 L 8 11" stroke="#e6e8ed" stroke-width="3" stroke-linecap="round" />
        <path d="M 0 3 L 0 28 M -8 11 L 8 11" stroke="#111115" stroke-width="1" fill="none" />
      </g>
    </g>

    <!-- Back Volume of Hair (dark silhouettes framing the head) -->
    <path d="M 170 420 C 140 280, 220 120, 360 110 C 500 120, 580 280, 550 420 C 560 520, 510 600, 480 620 C 470 540, 520 450, 490 360 C 440 210, 280 210, 230 360 C 200 450, 250 540, 240 620 C 210 600, 160 520, 170 420 Z" fill="#061211" />

    <!-- Head & Face Base Shape (Stylized smooth 3D jawline) -->
    <path d="M 210 400 C 205 280, 270 190, 360 190 C 450 190, 515 280, 510 400 C 505 480, 490 560, 435 630 C 400 670, 375 {chin_y}, 360 {chin_y} C 345 {chin_y}, 320 670, 285 630 C 230 560, 215 480, 210 400 Z" fill="url(#skinGrad)" />

    <!-- Violet/Purple Ambient Bounce Lighting on Chin & Jawline -->
    <path d="M 270 590 C 310 650, 340 {chin_y+10}, 360 {chin_y+10} C 380 {chin_y+10}, 410 650, 450 590 C 420 680, 380 710, 360 710 C 340 710, 300 680, 270 590 Z" fill="url(#purpleBounce)" />

    <!-- Stylized Nose -->
    <g transform="translate(360, {sunglasses_y + 120})">
      <!-- Nose bridge subtle shadow -->
      <path d="M -8 -45 C -5 -10, -18 10, -20 22 C -15 32, -4 34, 0 34 C 4 34, 15 32, 20 22 C 18 10, 5 -10, 8 -45" fill="#d98968" opacity="0.4" />
      <!-- Nose tip round highlight -->
      <ellipse cx="0" cy="22" rx="14" ry="10" fill="#fce5d8" />
      <!-- Nostrils definition -->
      <ellipse cx="-13" cy="25" rx="5" ry="3.5" fill="#541e2b" opacity="0.75" />
      <ellipse cx="13" cy="25" rx="5" ry="3.5" fill="#541e2b" opacity="0.75" />
      <path d="M -10 28 Q 0 34 10 28" stroke="#8a3c48" stroke-width="2.5" fill="none" stroke-linecap="round" />
    </g>

    <!-- Freckles across nose bridge and cheeks -->
    <g fill="#7e3b2e" opacity="0.55">
      <circle cx="330" cy="{sunglasses_y + 125}" r="1.8" />
      <circle cx="342" cy="{sunglasses_y + 132}" r="1.5" />
      <circle cx="355" cy="{sunglasses_y + 128}" r="1.6" />
      <circle cx="368" cy="{sunglasses_y + 130}" r="1.7" />
      <circle cx="380" cy="{sunglasses_y + 124}" r="1.4" />
      <circle cx="395" cy="{sunglasses_y + 134}" r="1.9" />
      <circle cx="315" cy="{sunglasses_y + 138}" r="1.6" />
      <circle cx="410" cy="{sunglasses_y + 136}" r="1.5" />
      <circle cx="300" cy="{sunglasses_y + 142}" r="1.8" />
      <circle cx="425" cy="{sunglasses_y + 140}" r="1.6" />
      <circle cx="348" cy="{sunglasses_y + 140}" r="1.3" />
      <circle cx="372" cy="{sunglasses_y + 138}" r="1.5" />
    </g>

    <!-- Full Stylized Lips -->
    <g transform="translate(360, {chin_y - 70})">
      <!-- Upper lip -->
      <path d="M -34 0 C -20 -8, -8 -8, 0 -3 C 8 -8, 20 -8, 34 0 C 20 6, 8 8, 0 8 C -8 8, -20 6, -34 0 Z" fill="#b85758" />
      <!-- Lip parting line -->
      <path d="M -32 1 Q 0 5 32 1" stroke="#4a1520" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <!-- Lower lip with 3D plump volume and gloss -->
      <path d="M -30 2 C -18 16, -10 24, 0 24 C 10 24, 18 16, 30 2 C 20 4, -20 4, -30 2 Z" fill="#d96c73" />
      <!-- Lip specular highlight -->
      <ellipse cx="-2" cy="14" rx="11" ry="4.5" fill="#fcd7db" opacity="0.75" />
    </g>

    <!-- Beauty Mark / Mole below left mouth corner -->
    <circle cx="406" cy="{chin_y - 45}" r="2.8" fill="#2d1620" />

    <!-- "Rebel" Gothic Script Tattoo on cheekbone below left sunglasses lens -->
    <g transform="translate(435, {tattoo_y}) rotate(12)">
      <!-- Gothic calligraphy path representation of "Rebel" -->
      <text x="0" y="0" font-family="'Old English Text MT', 'UnifrakturMaguntia', 'Blackletter', Georgia, serif" font-weight="900" font-size="28" fill="#15131a" letter-spacing="1">
        Rebel
      </text>
    </g>

    <!-- Eyebrows (Thick, stylized anime arch) -->
    <g transform="translate(360, {sunglasses_y - 30})">
      <!-- Right eyebrow (viewer left) -->
      <path d="M -135 15 Q -85 -10 -30 18 Q -85 -4 -135 15 Z" fill="#0c1e1e" />
      <!-- Left eyebrow (viewer right, slightly cocked rebel arch) -->
      <path d="M 30 18 Q 85 -12 135 12 Q 85 -5 30 18 Z" fill="#0c1e1e" />
    </g>

    <!-- RETRO-FUTURISTIC CHUNKY SUNGLASSES (Wrap-around cat-eye silhouette) -->
    <g transform="translate(360, {sunglasses_y})">
      
      <!-- Frame outer drop shadow on face -->
      <path d="M -160 10 C -150 -35, -50 -38, -15 -18 C -5 -12, 5 -12, 15 -18 C 50 -38, 150 -35, 160 10 C 165 48, 130 82, 60 74 C 25 70, 10 38, 0 38 C -10 38, -25 70, -60 74 C -130 82, -165 48, -160 10 Z" fill="#000000" opacity="0.4" filter="url(#shadowFilter)" />

      <!-- Thick Black Frame Base -->
      <path d="M -158 5 C -148 -35, -50 -36, -15 -16 C -5 -10, 5 -10, 15 -16 C 50 -36, 148 -35, 158 5 C 164 45, 128 78, 60 70 C 28 66, 12 36, 0 36 C -12 36, -28 66, -60 70 C -128 78, -164 45, -158 5 Z" fill="url(#frameGrad)" stroke="#111114" stroke-width="2.5" />

      <!-- Left Lens Cutout (viewer's left) -->
      <g>
        <clipPath id="lensClipL">
          <path d="M -145 5 C -138 -25, -58 -26, -24 -12 C -22 28, -48 60, -95 60 C -135 60, -150 35, -145 5 Z" />
        </clipPath>
        <!-- Dark Smoked Lens -->
        <path d="M -145 5 C -138 -25, -58 -26, -24 -12 C -22 28, -48 60, -95 60 C -135 60, -150 35, -145 5 Z" fill="url(#lensGrad)" />
        <!-- Softbox Studio Reflection inside Left Lens -->
        <g clip-path="url(#lensClipL)">
          <!-- Curved bright highlight strip reflecting studio lighting -->
          <ellipse cx="-85" cy="{refl_y + 12}" rx="65" ry="26" fill="url(#lensRefl)" transform="rotate(-15, -85, {refl_y + 12})" />
          <!-- Edge rim reflection -->
          <path d="M -140 8 C -130 -18, -60 -20, -30 -10" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="{0.55 * refl_opacity:.2f}" fill="none" />
        </g>
      </g>

      <!-- Right Lens Cutout (viewer's right) -->
      <g>
        <clipPath id="lensClipR">
          <path d="M 24 -12 C 58 -26, 138 -25, 145 5 C 150 35, 135 60, 95 60 C 48 60, 22 28, 24 -12 Z" />
        </clipPath>
        <!-- Dark Smoked Lens -->
        <path d="M 24 -12 C 58 -26, 138 -25, 145 5 C 150 35, 135 60, 95 60 C 48 60, 22 28, 24 -12 Z" fill="url(#lensGrad)" />
        <!-- Softbox Studio Reflection inside Right Lens -->
        <g clip-path="url(#lensClipR)">
          <!-- Curved bright highlight strip -->
          <ellipse cx="85" cy="{refl_y + 12}" rx="65" ry="26" fill="url(#lensRefl)" transform="rotate(15, 85, {refl_y + 12})" />
          <!-- Edge rim reflection -->
          <path d="M 30 -10 C 60 -20, 130 -18, 140 8" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="{0.55 * refl_opacity:.2f}" fill="none" />
        </g>
      </g>

      <!-- Frame Top Bridge Gloss Highlight -->
      <path d="M -135 -24 C -80 -28, -25 -14, 0 -10 C 25 -14, 80 -28, 135 -24" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" opacity="0.65" fill="none" />
    </g>

    <!-- VOLUMINOUS TEAL/PETROL HAIR WITH CYBER CYAN INNER GLOW -->
    <!-- Front wavy locks & layered bangs framing forehead -->
    <g>
      <!-- Deep base locks -->
      <path d="M 180 340 C 150 180, 240 {hair_crown_y - 80}, 360 {hair_crown_y - 80} C 480 {hair_crown_y - 80}, 570 180, 540 340 C 510 260, 460 210, 390 220 C 450 250, 480 310, 490 380 C 460 320, 410 280, 350 280 C 410 320, 420 380, 410 440 C 370 340, 310 310, 270 330 C 310 370, 310 430, 290 480 C 270 410, 240 360, 180 340 Z" fill="url(#hairDark)" />

      <!-- Center Wave Volume (flowing styled locks) -->
      <path d="M 230 240 C 280 160, 440 160, 490 240 C 440 200, 390 220, 360 250 C 330 220, 280 200, 230 240 Z" fill="#133d3b" />
      
      <!-- Cyan highlighted inner crown waves (that neon glow from reference) -->
      <path d="M 280 210 C 330 160, 390 160, 440 210 C 400 185, 360 190, 330 205 C 310 195, 295 200, 280 210 Z" fill="url(#cyanHighlight)" />
      
      <!-- Crown top fluff curls -->
      <path d="M 290 160 C 280 120, 340 100, 360 140 C 380 100, 440 120, 430 160 C 400 135, 320 135, 290 160 Z" fill="#0d2927" />

      <!-- Left sculpted lock (viewer right side) over ear -->
      <path d="M 480 320 C 530 350, 560 440, 530 520 C 510 460, 480 430, 470 390 C 485 365, 480 340, 480 320 Z" fill="#081817" />
      <!-- Right sculpted lock (viewer left side) -->
      <path d="M 240 320 C 190 350, 160 440, 190 520 C 210 460, 240 430, 250 390 C 235 365, 240 340, 240 320 Z" fill="#081817" />

      <!-- Fine hair strand highlights -->
      <path d="M 330 150 Q 360 180 370 230" stroke="#3af0e0" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.6" />
      <path d="M 305 185 Q 345 210 350 255" stroke="#3af0e0" stroke-width="1.8" stroke-linecap="round" fill="none" opacity="0.5" />
      <path d="M 415 185 Q 375 210 370 255" stroke="#3af0e0" stroke-width="1.8" stroke-linecap="round" fill="none" opacity="0.5" />
      <path d="M 260 250 Q 300 280 320 340" stroke="#1da89b" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.7" />
      <path d="M 460 250 Q 420 280 400 340" stroke="#1da89b" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.7" />
    </g>

  </g>
</svg>"""
    return svg

if __name__ == '__main__':
    with open('/tmp/frame_0.svg', 'w') as f:
        f.write(generate_svg(0.0))
    print("Frame 0 generated successfully")
