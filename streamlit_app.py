<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baguio Itinerary | Benguet Prime Hotel</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Font: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        pine: {
                            950: '#0a291f',
                            900: '#0f3d2e',
                            800: '#194f3c',
                            700: '#256149',
                            100: '#e6f2ed',
                            50: '#f3f9f6',
                        }
                    }
                }
            }
        }
    </script>
</head>
<body id="page-body" class="bg-slate-50 text-slate-800 font-sans antialiased selection:bg-pine-700 selection:text-white min-h-screen flex flex-col transition-colors duration-300 bg-cover bg-center bg-fixed">

    <!-- Optional Background Image Overlay for Readability -->
    <div id="bg-image-overlay" class="fixed inset-0 bg-slate-950/45 backdrop-blur-[2px] pointer-events-none hidden z-0 transition-opacity duration-300"></div>

    <!-- Main Container -->
    <main class="relative z-10 max-w-4xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-10 flex-grow">

        <!-- Interactive Background / Theme Switcher Bar -->
        <section id="theme-bar" aria-label="Background and Theme Switcher" class="bg-white/90 backdrop-blur-md rounded-2xl p-3.5 sm:p-4 shadow-sm border border-slate-200/80 mb-6 transition-colors duration-300">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                <div class="flex items-center gap-2 shrink-0">
            
                    <span id="theme-bar-label" class="text-xs sm:text-sm font-bold text-slate-800 tracking-tight">Page Background:</span>
                </div>

                <!-- Baguio Presets & Custom Controls -->
                <div class="flex flex-wrap items-center gap-2">
                    <button type="button" onclick="applyBgPreset('fog')" data-preset="fog" title="Morning Fog Soft Gray"
                            class="preset-btn inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer bg-slate-100 text-slate-800 border-slate-300">
                        <span class="w-3 h-3 rounded-full bg-slate-100 border border-slate-400"></span>
                        Morning Fog
                    </button>

                    <button type="button" onclick="applyBgPreset('crisp')" data-preset="crisp" title="Crisp White"
                            class="preset-btn inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer bg-white text-slate-800 border-slate-300">
                        <span class="w-3 h-3 rounded-full bg-white border border-slate-400"></span>
                        Crisp White
                    </button>

                    <button type="button" onclick="applyBgPreset('cabin')" data-preset="cabin" title="Warm Cabin Cream"
                            class="preset-btn inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer bg-amber-50 text-amber-950 border-amber-200">
                        <span class="w-3 h-3 rounded-full bg-[#fdf8f0] border border-amber-400"></span>
                        Warm Cabin
                    </button>

                    <button type="button" onclick="applyBgPreset('pine')" data-preset="pine" title="Misty Pine Forest"
                            class="preset-btn inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer bg-emerald-900 text-white border-emerald-700">
                        <span class="w-3 h-3 rounded-full bg-[#0b2e23] border border-emerald-400"></span>
                        Misty Pine
                    </button>

                    <button type="button" onclick="applyBgPreset('midnight')" data-preset="midnight" title="Midnight Starry Baguio"
                            class="preset-btn inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer bg-slate-900 text-slate-100 border-slate-700">
                        <span class="w-3 h-3 rounded-full bg-slate-950 border border-indigo-400"></span>
                        Midnight Baguio
                    </button>

                    <!-- Custom Color Picker -->
                    <label title="Pick Custom Solid Background Color"
                           class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full text-xs font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 cursor-pointer transition-colors">
                        <input id="custom-color-input" type="color" value="#f8fafc" oninput="applyCustomColor(this.value)"
                               class="w-4 h-4 rounded-full border-0 p-0 bg-transparent cursor-pointer" />
                        <span>Color</span>
                    </label>

                    <!-- Toggle Custom Image URL Drawer -->
                    <button type="button" onclick="toggleImageDrawer()" id="toggle-img-drawer-btn"
                            class="inline-flex items-center gap-1 px-3 py-1.5 rounded-full text-xs font-semibold border border-slate-300 bg-white text-slate-700 hover:bg-slate-50 cursor-pointer transition-colors">
                        <span>🖼️ Image URL</span>
                    </button>
                </div>
            </div>

            <!-- Collapsible Custom Background Image URL Input -->
            <div id="custom-image-drawer" class="hidden mt-3 pt-3 border-t border-slate-200/80 flex flex-col sm:flex-row gap-2">
                <input id="custom-image-url" type="url" placeholder="Paste background image URL (e.g., https://images.unsplash.com/...)"
                       class="flex-grow px-3.5 py-2 rounded-xl text-xs sm:text-sm border border-slate-300 bg-white text-slate-800 focus:outline-none focus:ring-2 focus:ring-pine-700" />
                <div class="flex gap-2">
                    <button type="button" onclick="applyCustomImage()"
                            class="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-pine-900 text-white hover:bg-pine-800 transition-colors cursor-pointer">
                        Apply Image
                    </button>
                    <button type="button" onclick="applyBgPreset('fog')"
                            class="px-3 py-2 rounded-xl text-xs sm:text-sm font-medium bg-slate-100 text-slate-700 hover:bg-slate-200 transition-colors cursor-pointer">
                        Clear
                    </button>
                </div>
            </div>
        </section>

        <!-- Header Box with Dark Forest Green Gradient -->
        <header class="rounded-2xl p-6 sm:p-10 text-white text-center shadow-xl mb-8 relative overflow-hidden"
                style="background: linear-gradient(135deg, #0f3d2e, #256149);">
            <!-- Subtle decorative pine/mountain circles -->
            <div class="absolute -top-12 -right-12 w-48 h-48 bg-white/5 rounded-full pointer-events-none"></div>
            <div class="absolute -bottom-16 -left-10 w-56 h-56 bg-white/5 rounded-full pointer-events-none"></div>

            <div class="relative z-10">
                <h1 class="text-2xl sm:text-4xl font-extrabold tracking-tight mb-2">
                    🌲 Baguio Adventure Itinerary
                </h1>
                <p class="text-emerald-100 text-base sm:text-lg font-medium mb-6">
                    Pre-Check-In &amp; Day 1 Visual Guide
                </p>

                <!-- Pill Badges -->
                <div class="flex flex-wrap justify-center gap-2.5 sm:gap-3">
                    <span class="inline-flex items-center px-4 py-1.5 rounded-full text-xs sm:text-sm font-medium bg-white/20 backdrop-blur-sm border border-white/15 shadow-sm">
                        🚌 Arrival: 5:55 AM
                    </span>
                    <span class="inline-flex items-center px-4 py-1.5 rounded-full text-xs sm:text-sm font-medium bg-white/20 backdrop-blur-sm border border-white/15 shadow-sm">
                        🏨 Benguet Prime Hotel
                    </span>
                    <span class="inline-flex items-center px-4 py-1.5 rounded-full text-xs sm:text-sm font-medium bg-white/20 backdrop-blur-sm border border-white/15 shadow-sm">
                        🔑 Check-in: 2:00 PM
                    </span>
                </div>
            </div>
        </header>

        <!-- Overall Trip Progress Summary Bar -->
        <section id="progress-card" aria-label="Trip Progress" class="bg-white rounded-2xl p-5 shadow-sm border border-slate-200/80 mb-8 transition-colors duration-300">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
                <div>
                    <h2 id="progress-heading" class="text-sm font-bold text-slate-800 uppercase tracking-wider">Day 1 Adventure Progress</h2>
                    <p id="progress-subtext" class="text-xs text-slate-500">Tap any stop card's button to mark it as visited</p>
                </div>
                <div class="flex items-center gap-3">
                    <span id="stops-progress-text" class="text-sm font-bold text-pine-900 bg-pine-50 px-3 py-1 rounded-full border border-pine-100">
                        0 of 7 Stops Visited
                    </span>
                    <button id="reset-all-btn" type="button" onclick="resetProgress()" 
                            class="text-xs font-medium text-slate-400 hover:text-rose-600 transition-colors px-2 py-1 rounded-lg hover:bg-rose-50 hidden">
                        Reset
                    </button>
                </div>
            </div>
            <div id="stops-progress-track" class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden">
                <div id="stops-progress-bar" class="bg-gradient-to-r from-pine-900 to-pine-700 h-2.5 rounded-full transition-all duration-500 ease-out" style="width: 0%"></div>
            </div>
        </section>

        <!-- Day 1 Schedule Section -->
        <section aria-labelledby="schedule-heading" class="mb-12">
            <div class="flex items-center justify-between mb-5">
                <h2 id="schedule-heading" class="text-xl sm:text-2xl font-bold text-slate-900 flex items-center gap-2 transition-colors">
                    <span>⏰</span> Day 1 Schedule
                </h2>
                <span id="schedule-location-hint" class="text-xs font-medium text-slate-500 hidden sm:inline-block transition-colors">F. Calderon St. &amp; Baguio City Center</span>
            </div>

            <!-- Stops Container -->
            <div id="stops-container" class="space-y-5">
                <!-- Cards injected via JavaScript -->
            </div>
        </section>

        <hr id="section-divider" class="border-slate-200 my-10 transition-colors">

        <!-- Interactive Packing Checklist Section -->
        <section id="packing-card" aria-labelledby="checklist-heading" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200/80 mb-8 transition-colors duration-300">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-5">
                <div>
                    <h2 id="checklist-heading" class="text-xl sm:text-2xl font-bold text-slate-900 flex items-center gap-2">
                        <span>🎒</span> Interactive Packing Checklist
                    </h2>
                    <p id="checklist-subtext" class="text-sm text-slate-500 mt-1">Make sure you're ready for Baguio's cool mountain weather.</p>
                </div>
                <div class="self-start sm:self-center">
                    <span id="packing-badge" class="inline-flex items-center px-3.5 py-1.5 rounded-full text-xs font-bold bg-amber-50 text-amber-700 border border-amber-200">
                        0 / 6 Packed
                    </span>
                </div>
            </div>

            <!-- Packing Progress Bar -->
            <div id="packing-progress-track" class="w-full bg-slate-100 rounded-full h-2 mb-6 overflow-hidden">
                <div id="packing-progress-bar" class="bg-amber-500 h-2 rounded-full transition-all duration-500 ease-out" style="width: 0%"></div>
            </div>

            <!-- Checklist Items -->
            <div id="checklist-container" class="space-y-3">
                <!-- Checklist items injected via JavaScript -->
            </div>
        </section>

        <!-- Toast Notification Message Box (Replaces alert) -->
        <div id="toast-box" role="status" aria-live="polite"
             class="fixed bottom-5 right-5 left-5 sm:left-auto sm:w-80 bg-pine-900 text-white px-4 py-3 rounded-xl shadow-lg border border-white/10 transform translate-y-24 opacity-0 transition-all duration-300 z-50 flex items-center gap-3 pointer-events-none">
            <span id="toast-icon" class="text-lg">🌲</span>
            <p id="toast-message" class="text-sm font-medium"></p>
        </div>

    </main>

    <!-- Footer -->
    <footer id="page-footer" class="relative z-10 py-6 text-center text-slate-500 text-sm border-t border-slate-200/70 bg-white/60 backdrop-blur-sm transition-colors duration-300">
        <p class="font-medium">Safe travels to the Summer Capital of the Philippines! 🌲</p>
    </footer>

    <script>
        // Itinerary Data
        const stopsData = [
            {
                id: "stop-1",
                time: "5:55 AM – 6:30 AM",
                title: "1. Luggage Drop-Off at Benguet Prime Hotel",
                desc: "Head directly to Benguet Prime Hotel on F. Calderon St. Leave your bags at the front desk so you can explore hands-free.",
                img: "https://images.unsplash.com/photo-1590490360182-c33d57733427?q=80&w=800&auto=format&fit=crop",
                fallbackText: "Benguet+Prime+Hotel",
                tag: "Check-in Prep"
            },
            {
                id: "stop-2",
                time: "6:30 AM – 8:30 AM",
                title: "2. Breakfast at Good Taste Restaurant",
                desc: "Fuel up with a hearty breakfast and experience getting your food served by their robot crew.",
                img: "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                fallbackText: "Good+Taste+Restaurant",
                tag: "Food & Dining"
            },
            {
                id: "stop-3",
                time: "8:30 AM – 9:30 AM",
                title: "3. Morning Stroll at Burnham Park",
                desc: "Enjoy the crisp morning air around Burnham Lagoon before the daytime crowds arrive.",
                img: "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRlPzvf2Z6akTze8mMI6vWj0c21cNJKZ7xpk7PzN9jC_oyJhUNmuc76oe3i5cu6MoqfbigGFGGeiK1I0K0",
                fallbackText: "Burnham+Park+Lagoon",
                tag: "Nature & Park"
            },
            {
                id: "stop-4",
                time: "10:00 AM – 1:00 PM",
                title: "4. Ili-Likha Artists Village",
                desc: "Explore this hidden food and art park filled with woodwork, sculptures, stained glass art, and cozy cafes.",
                img: "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                fallbackText: "Ili-Likha+Artists+Village",
                tag: "Art & Culture"
            },
            {
                id: "stop-5",
                time: "1:30 PM – 2:00 PM",
                title: "5. Hotel Check-In & Rest",
                desc: "Return to Benguet Prime Hotel to claim your luggage, check into your room, and rest up.",
                img: "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=800&auto=format&fit=crop",
                fallbackText: "Hotel+Check-In",
                tag: "Rest & Recharge"
            },
            {
                id: "stop-6",
                time: "6:00 PM – 8:30 PM",
                title: "6. SM City Baguio & Dinner",
                desc: "Enjoy the cool evening breeze and panoramic city views from the open-air terraces of SM Baguio.",
                img: "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0",
                fallbackText: "SM+City+Baguio",
                tag: "City Views & Dinner"
            },
            {
                id: "stop-7",
                time: "9:00 PM – 10:00 PM",
                title: "7. Baguio Night Market (Harrison Road)",
                desc: "Browse through ukay-ukay thrift stalls and sample hot street food just a short walk from the hotel.",
                img: "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I",
                fallbackText: "Baguio+Night+Market",
                tag: "Nightlife & Street Food"
            }
        ];

        // Packing Checklist Data
        const checklistData = [
            { id: "pack-1", text: "Light jacket or sweater (Crucial: Baguio mornings & evenings get chilly!)" },
            { id: "pack-2", text: "Comfortable walking shoes (For parks & uphill walks)" },
            { id: "pack-3", text: "Reusable water bottle" },
            { id: "pack-4", text: "Compact umbrella or light rain gear" },
            { id: "pack-5", text: "Power bank and charging cables" },
            { id: "pack-6", text: "Cash & small bills (For taxis, jeepneys, and Night Market stalls)" }
        ];

        // State management with localStorage persistence
        const STORAGE_KEY = "baguio_itinerary_state_v1";
        let state = {
            visitedStops: {},
            packedItems: {},
            bgTheme: {
                mode: "preset", // 'preset' | 'color' | 'image'
                value: "fog",
                isDark: false
            }
        };

        // Baguio Background Presets
        const bgPresets = {
            fog: {
                label: "Morning Fog",
                bgColor: "#f8fafc",
                isDark: false
            },
            crisp: {
                label: "Crisp White",
                bgColor: "#ffffff",
                isDark: false
            },
            cabin: {
                label: "Warm Cabin",
                bgColor: "#fdf8f0",
                isDark: false
            },
            pine: {
                label: "Misty Pine",
                bgColor: "#0a291f",
                isDark: true
            },
            midnight: {
                label: "Midnight Baguio",
                bgColor: "#0f172a",
                isDark: true
            }
        };

        // Helper: Determine if a hex color is dark for automatic contrast adaptation
        function isHexColorDark(hex) {
            const clean = hex.replace("#", "");
            if (clean.length !== 6) return false;
            const r = parseInt(clean.substring(0, 2), 16);
            const g = parseInt(clean.substring(2, 4), 16);
            const b = parseInt(clean.substring(4, 6), 16);
            // Perceived luminance formula
            const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
            return luminance < 0.52;
        }

        // Load saved state safely
        function loadState() {
            try {
                const saved = localStorage.getItem(STORAGE_KEY);
                if (saved) {
                    const parsed = JSON.parse(saved);
                    state.visitedStops = parsed.visitedStops || {};
                    state.packedItems = parsed.packedItems || {};
                    if (parsed.bgTheme) {
                        state.bgTheme = parsed.bgTheme;
                    }
                }
            } catch (e) {
                console.warn("Could not load state from localStorage:", e);
            }
        }

        // Save state safely
        function saveState() {
            try {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
            } catch (e) {
                console.warn("Could not save state to localStorage:", e);
            }
        }

        // Apply Background & Adaptive Surface Contrast
        function applyBackgroundTheme(save = true) {
            const body = document.getElementById("page-body");
            const overlay = document.getElementById("bg-image-overlay");
            const { mode, value } = state.bgTheme;

            let isDark = false;

            if (mode === "preset") {
                const preset = bgPresets[value] || bgPresets.fog;
                body.style.backgroundImage = "none";
                body.style.backgroundColor = preset.bgColor;
                overlay.classList.add("hidden");
                isDark = preset.isDark;
            } else if (mode === "color") {
                body.style.backgroundImage = "none";
                body.style.backgroundColor = value;
                overlay.classList.add("hidden");
                isDark = isHexColorDark(value);
                document.getElementById("custom-color-input").value = value;
            } else if (mode === "image") {
                body.style.backgroundColor = "#0f172a";
                body.style.backgroundImage = `url('${value}')`;
                overlay.classList.remove("hidden");
                isDark = true;
                document.getElementById("custom-image-url").value = value;
            }

            state.bgTheme.isDark = isDark;

            // Highlight active preset button
            document.querySelectorAll(".preset-btn").forEach((btn) => {
                const active = mode === "preset" && btn.dataset.preset === value;
                btn.classList.toggle("ring-2", active);
                btn.classList.toggle("ring-amber-500", active);
                btn.classList.toggle("ring-offset-1", active);
            });

            // Adapt Theme Bar, Progress Bar, Headings, Divider, and Footer for Dark/Light Backgrounds
            const themeBar = document.getElementById("theme-bar");
            const themeBarLabel = document.getElementById("theme-bar-label");
            const progressCard = document.getElementById("progress-card");
            const progressHeading = document.getElementById("progress-heading");
            const progressSubtext = document.getElementById("progress-subtext");
            const stopsProgressTrack = document.getElementById("stops-progress-track");
            const scheduleHeading = document.getElementById("schedule-heading");
            const scheduleHint = document.getElementById("schedule-location-hint");
            const divider = document.getElementById("section-divider");
            const packingCard = document.getElementById("packing-card");
            const checklistHeading = document.getElementById("checklist-heading");
            const checklistSubtext = document.getElementById("checklist-subtext");
            const packingProgressTrack = document.getElementById("packing-progress-track");
            const footer = document.getElementById("page-footer");

            if (isDark) {
                themeBar.className = "bg-slate-900/85 backdrop-blur-md rounded-2xl p-3.5 sm:p-4 shadow-lg border border-slate-700/80 mb-6 transition-colors duration-300";
                themeBarLabel.className = "text-xs sm:text-sm font-bold text-slate-100 tracking-tight";

                progressCard.className = "bg-slate-900/90 backdrop-blur-md rounded-2xl p-5 shadow-md border border-slate-700/80 mb-8 transition-colors duration-300";
                progressHeading.className = "text-sm font-bold text-slate-100 uppercase tracking-wider";
                progressSubtext.className = "text-xs text-slate-400";
                stopsProgressTrack.className = "w-full bg-slate-800 rounded-full h-2.5 overflow-hidden";

                scheduleHeading.className = "text-xl sm:text-2xl font-bold text-white flex items-center gap-2 transition-colors drop-shadow-xs";
                scheduleHint.className = "text-xs font-medium text-slate-300 hidden sm:inline-block transition-colors";
                divider.className = "border-slate-700/80 my-10 transition-colors";

                packingCard.className = "bg-slate-900/90 backdrop-blur-md rounded-2xl p-6 sm:p-8 shadow-md border border-slate-700/80 mb-8 transition-colors duration-300";
                checklistHeading.className = "text-xl sm:text-2xl font-bold text-white flex items-center gap-2";
                checklistSubtext.className = "text-sm text-slate-400 mt-1";
                packingProgressTrack.className = "w-full bg-slate-800 rounded-full h-2 mb-6 overflow-hidden";

                footer.className = "relative z-10 py-6 text-center text-slate-300 text-sm border-t border-slate-800 bg-slate-950/75 backdrop-blur-md transition-colors duration-300";
            } else {
                themeBar.className = "bg-white/90 backdrop-blur-md rounded-2xl p-3.5 sm:p-4 shadow-sm border border-slate-200/80 mb-6 transition-colors duration-300";
                themeBarLabel.className = "text-xs sm:text-sm font-bold text-slate-800 tracking-tight";

                progressCard.className = "bg-white rounded-2xl p-5 shadow-sm border border-slate-200/80 mb-8 transition-colors duration-300";
                progressHeading.className = "text-sm font-bold text-slate-800 uppercase tracking-wider";
                progressSubtext.className = "text-xs text-slate-500";
                stopsProgressTrack.className = "w-full bg-slate-100 rounded-full h-2.5 overflow-hidden";

                scheduleHeading.className = "text-xl sm:text-2xl font-bold text-slate-900 flex items-center gap-2 transition-colors";
                scheduleHint.className = "text-xs font-medium text-slate-500 hidden sm:inline-block transition-colors";
                divider.className = "border-slate-200 my-10 transition-colors";

                packingCard.className = "bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200/80 mb-8 transition-colors duration-300";
                checklistHeading.className = "text-xl sm:text-2xl font-bold text-slate-900 flex items-center gap-2";
                checklistSubtext.className = "text-sm text-slate-500 mt-1";
                packingProgressTrack.className = "w-full bg-slate-100 rounded-full h-2 mb-6 overflow-hidden";

                footer.className = "relative z-10 py-6 text-center text-slate-500 text-sm border-t border-slate-200/70 bg-white/60 backdrop-blur-sm transition-colors duration-300";
            }

            if (save) {
                saveState();
            }
            renderStops();
            renderChecklist();
        }

        function applyBgPreset(presetKey) {
            state.bgTheme = {
                mode: "preset",
                value: presetKey,
                isDark: bgPresets[presetKey]?.isDark || false
            };
            applyBackgroundTheme(true);
            showToast(`Background set to ${bgPresets[presetKey].label}`, "🎨");
        }

        function applyCustomColor(hexColor) {
            state.bgTheme = {
                mode: "color",
                value: hexColor,
                isDark: isHexColorDark(hexColor)
            };
            applyBackgroundTheme(true);
        }

        function toggleImageDrawer() {
            const drawer = document.getElementById("custom-image-drawer");
            drawer.classList.toggle("hidden");
        }

        function applyCustomImage() {
            const urlInput = document.getElementById("custom-image-url").value.trim();
            if (!urlInput) {
                showToast("Please paste a valid image URL first.", "⚠️");
                return;
            }
            // Test image loading before applying
            const testImg = new Image();
            testImg.onload = () => {
                state.bgTheme = {
                    mode: "image",
                    value: urlInput,
                    isDark: true
                };
                applyBackgroundTheme(true);
                showToast("Custom background image applied!", "🖼️");
            };
            testImg.onerror = () => {
                showToast("Could not load that image URL. Try another link.", "❌");
            };
            testImg.src = urlInput;
        }

        // Toast Notification Helper
        let toastTimeout;
        function showToast(message, icon = "🌲") {
            const toastBox = document.getElementById("toast-box");
            const toastMsg = document.getElementById("toast-message");
            const toastIcon = document.getElementById("toast-icon");

            toastMsg.textContent = message;
            toastIcon.textContent = icon;

            toastBox.classList.remove("translate-y-24", "opacity-0");
            toastBox.classList.add("translate-y-0", "opacity-100");

            clearTimeout(toastTimeout);
            toastTimeout = setTimeout(() => {
                toastBox.classList.remove("translate-y-0", "opacity-100");
                toastBox.classList.add("translate-y-24", "opacity-0");
            }, 2600);
        }

        // Render Itinerary Cards
        function renderStops() {
            const container = document.getElementById("stops-container");
            container.innerHTML = "";
            const isDark = !!state.bgTheme.isDark;

            stopsData.forEach((stop) => {
                const isVisited = !!state.visitedStops[stop.id];
                const fallbackUrl = `https://placehold.co/600x400/0f3d2e/ffffff?text=${stop.fallbackText}`;

                const card = document.createElement("article");
                if (isDark) {
                    card.className = `group rounded-2xl border transition-all duration-300 overflow-hidden shadow-md hover:shadow-lg backdrop-blur-md ${
                        isVisited
                            ? "bg-emerald-950/80 border-emerald-700/70"
                            : "bg-slate-900/90 border-slate-700/80 hover:border-emerald-500/50"
                    }`;
                } else {
                    card.className = `group bg-white rounded-2xl border transition-all duration-300 overflow-hidden shadow-sm hover:shadow-md ${
                        isVisited 
                            ? "border-emerald-300 bg-emerald-50/20" 
                            : "border-slate-200/90 hover:border-pine-700/40"
                    }`;
                }

                card.innerHTML = `
                    <div class="flex flex-col sm:flex-row">
                        <!-- Image Column (1/3 width on desktop) -->
                        <div class="sm:w-1/3 relative overflow-hidden ${isDark ? 'bg-slate-800' : 'bg-slate-200'} min-h-[190px] sm:min-h-[210px]">
                            <img 
                                src="${stop.img}" 
                                alt="${stop.title}"
                                loading="lazy"
                                onerror="this.onerror=null; this.src='${fallbackUrl}';"
                                class="w-full h-full object-cover object-center transition-transform duration-500 group-hover:scale-105 ${isVisited ? 'opacity-80' : ''}"
                            />
                            <span class="absolute top-3 left-3 bg-slate-900/80 backdrop-blur-xs text-white text-[11px] font-semibold px-2.5 py-1 rounded-full">
                                ${stop.tag}
                            </span>
                        </div>

                        <!-- Details Column (2/3 width on desktop) -->
                        <div class="sm:w-2/3 p-5 sm:p-6 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between gap-2 mb-1.5">
                                    <span class="${isDark ? 'text-amber-400' : 'text-amber-600'} font-bold text-xs sm:text-sm uppercase tracking-wider">
                                        ${stop.time}
                                    </span>
                                    ${isVisited ? `
                                        <span class="inline-flex items-center gap-1 text-xs font-bold ${isDark ? 'text-emerald-300 bg-emerald-900/80 border border-emerald-700/60' : 'text-emerald-700 bg-emerald-100'} px-2.5 py-0.5 rounded-full">
                                            ✓ Visited
                                        </span>
                                    ` : ""}
                                </div>

                                <h3 class="text-lg sm:text-xl font-bold mb-2 leading-snug ${
                                    isDark
                                        ? (isVisited ? 'line-through decoration-emerald-400/60 text-slate-400' : 'text-white')
                                        : (isVisited ? 'line-through decoration-emerald-600/50 text-slate-600' : 'text-slate-900')
                                }">
                                    ${stop.title}
                                </h3>

                                <p class="${isDark ? 'text-slate-300' : 'text-slate-600'} text-sm sm:text-base leading-relaxed">
                                    ${stop.desc}
                                </p>
                            </div>

                            <div class="mt-5 pt-4 border-t ${isDark ? 'border-slate-800' : 'border-slate-100'} flex items-center justify-end">
                                <button 
                                    type="button"
                                    onclick="toggleStop('${stop.id}')"
                                    class="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 cursor-pointer select-none ${
                                        isVisited
                                            ? "bg-emerald-600 text-white hover:bg-emerald-700 shadow-xs"
                                            : (isDark
                                                ? "bg-slate-800 text-slate-200 hover:bg-pine-700 hover:text-white"
                                                : "bg-slate-100 text-slate-700 hover:bg-pine-900 hover:text-white")
                                    }"
                                >
                                    <span>${isVisited ? "✓ Completed" : "○ Mark as Visited"}</span>
                                </button>
                            </div>
                        </div>
                    </div>
                `;

                container.appendChild(card);
            });

            updateStopsProgress();
        }

        // Toggle Stop Visited State
        function toggleStop(stopId) {
            const stop = stopsData.find(s => s.id === stopId);
            if (!stop) return;

            state.visitedStops[stopId] = !state.visitedStops[stopId];
            saveState();
            renderStops();

            if (state.visitedStops[stopId]) {
                showToast(`Visited: ${stop.title.replace(/^\d+\.\s*/, '')}`, "✅");
            }
        }

        // Update Stops Progress Bar
        function updateStopsProgress() {
            const total = stopsData.length;
            const visitedCount = stopsData.filter(s => state.visitedStops[s.id]).length;
            const percentage = Math.round((visitedCount / total) * 100);

            document.getElementById("stops-progress-text").textContent = `${visitedCount} of ${total} Stops Visited`;
            document.getElementById("stops-progress-bar").style.width = `${percentage}%`;

            const resetBtn = document.getElementById("reset-all-btn");
            const packedCount = checklistData.filter(c => state.packedItems[c.id]).length;
            if (visitedCount > 0 || packedCount > 0) {
                resetBtn.classList.remove("hidden");
            } else {
                resetBtn.classList.add("hidden");
            }
        }

        // Render Packing Checklist
        function renderChecklist() {
            const container = document.getElementById("checklist-container");
            container.innerHTML = "";
            const isDark = !!state.bgTheme.isDark;

            checklistData.forEach((item) => {
                const isChecked = !!state.packedItems[item.id];

                const label = document.createElement("label");
                if (isDark) {
                    label.className = `flex items-start sm:items-center gap-3.5 p-3.5 rounded-xl border transition-all duration-200 cursor-pointer select-none ${
                        isChecked
                            ? "bg-emerald-950/60 border-emerald-700/50 text-slate-400"
                            : "bg-slate-800/70 hover:bg-slate-800 border-slate-700/80 text-slate-200"
                    }`;
                } else {
                    label.className = `flex items-start sm:items-center gap-3.5 p-3.5 rounded-xl border transition-all duration-200 cursor-pointer select-none ${
                        isChecked
                            ? "bg-pine-50/70 border-pine-700/30 text-slate-500"
                            : "bg-slate-50/60 hover:bg-slate-100/80 border-slate-200/80 text-slate-800"
                    }`;
                }

                label.innerHTML = `
                    <input 
                        type="checkbox" 
                        ${isChecked ? "checked" : ""}
                        onchange="toggleChecklistItem('${item.id}')"
                        class="mt-0.5 sm:mt-0 w-5 h-5 rounded-md border-slate-300 text-pine-900 focus:ring-pine-700 accent-[#0f3d2e] cursor-pointer shrink-0"
                    />
                    <span class="text-sm sm:text-base font-medium leading-snug ${isChecked ? (isDark ? 'line-through text-slate-500' : 'line-through text-slate-400') : ''}">
                        ${item.text}
                    </span>
                `;

                container.appendChild(label);
            });

            updatePackingProgress();
        }

        // Toggle Packing Item
        function toggleChecklistItem(itemId) {
            state.packedItems[itemId] = !state.packedItems[itemId];
            saveState();
            renderChecklist();
            updateStopsProgress();

            const packedCount = checklistData.filter(c => state.packedItems[c.id]).length;
            if (packedCount === checklistData.length && state.packedItems[itemId]) {
                showToast("All packed and ready for Baguio!", "🎒");
            }
        }

        // Update Packing Progress Bar
        function updatePackingProgress() {
            const total = checklistData.length;
            const packedCount = checklistData.filter(c => state.packedItems[c.id]).length;
            const percentage = Math.round((packedCount / total) * 100);

            const badge = document.getElementById("packing-badge");
            badge.textContent = `${packedCount} / ${total} Packed`;

            if (packedCount === total) {
                badge.className = "inline-flex items-center px-3.5 py-1.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200";
            } else {
                badge.className = "inline-flex items-center px-3.5 py-1.5 rounded-full text-xs font-bold bg-amber-50 text-amber-700 border border-amber-200";
            }

            document.getElementById("packing-progress-bar").style.width = `${percentage}%`;
        }

        // Reset All Progress
        function resetProgress() {
            state.visitedStops = {};
            state.packedItems = {};
            saveState();
            renderStops();
            renderChecklist();
            showToast("Progress reset for a fresh trip!", "🔄");
        }

        // Initialize Dashboard
        window.addEventListener("DOMContentLoaded", () => {
            loadState();
            applyBackgroundTheme(false);
        });
    </script>
</body>
</html>
