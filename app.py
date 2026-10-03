<!DOCTYPE html>ư
st.image("logo.jpg")
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NexusBank Pro - Ngân hàng quỷ santan</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Pro/Free Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        bank: {
                            dark: '#071124',
                            primary: '#0F2744',
                            accent: '#2563EB',
                            gold: '#D97706',
                            cardbg: '#112240',
                            surface: '#0B192C'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif']
                    }
                }
            }
        }
    </script>
    <style>
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #071124;
        }
        ::-webkit-scrollbar-thumb {
            background: #1E3A8A;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #3B82F6;
        }
        .glass-panel {
            background: rgba(17, 34, 64, 0.7);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(59, 130, 246, 0.15);
        }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-950 via-bank-dark to-slate-900 text-slate-100 font-sans min-h-screen flex flex-col md:flex-row antialiased selection:bg-blue-600 selection:text-white">

    <aside class="w-full md:w-64 bg-slate-900/95 backdrop-blur-xl border-r border-slate-800 flex flex-col justify-between p-5 sticky top-0 md:h-screen z-50">
        <div>
            <!-- Brand Logo -->
            <div class="flex items-center space-x-3 mb-8 px-2">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-amber-500 flex items-center justify-center shadow-lg shadow-blue-600/30">
                    <i class="fa-solid fa-building-columns text-white text-lg"></i>
                </div>
                <div>
                    <h1 class="font-bold text-lg tracking-wide text-white">NEXUS<span class="text-amber-400">BANK</span></h1>
                    <p class="text-[11px] text-slate-400">Digital Banking Elite</p>
                </div>
            </div>

            <!-- Navigation Links -->
            <nav class="space-y-1.5">
                <a href="#dashboard" onclick="switchTab('dashboard')" id="nav-dashboard" class="flex items-center space-x-3 px-4 py-3 rounded-xl bg-blue-600 text-white font-medium shadow-lg shadow-blue-600/30 transition-all">
                    <i class="fa-solid fa-chart-pie w-5 text-center"></i>
                    <span>Tổng Quan</span>
                </a>
                <a href="#transfer" onclick="switchTab('transfer')" id="nav-transfer" class="flex items-center space-x-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800/60 font-medium transition-all">
                    <i class="fa-solid fa-right-left w-5 text-center"></i>
                    <span>Chuyển Khoản</span>
                </a>
                <a href="#savings" onclick="switchTab('savings')" id="nav-savings" class="flex items-center space-x-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800/60 font-medium transition-all">
                    <i class="fa-solid fa-piggy-bank w-5 text-center"></i>
                    <span>Tiết Kiệm Online</span>
                </a>
                <a href="#cards" onclick="switchTab('cards')" id="nav-cards" class="flex items-center space-x-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800/60 font-medium transition-all">
                    <i class="fa-solid fa-credit-card w-5 text-center"></i>
                    <span>Thẻ Ngân Hàng</span>
                </a>
                <a href="#history" onclick="switchTab('history')" id="nav-history" class="flex items-center space-x-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800/60 font-medium transition-all">
                    <i class="fa-solid fa-clock-rotate-left w-5 text-center"></i>
                    <span>Lịch Sử Giao Dịch</span>
                </a>
            </nav>
        </div>

        <!-- Sidebar Footer & User Profile Toolbar -->
        <div class="pt-6 border-t border-slate-800/80 space-y-3">
            <button onclick="openSupportModal()" class="w-full flex items-center justify-between p-3 rounded-xl bg-slate-800/50 hover:bg-slate-800 text-slate-300 hover:text-white transition-all text-sm border border-slate-700/50">
                <span class="flex items-center space-x-2.5">
                    <i class="fa-solid fa-headset text-amber-400"></i>
                    <span>Hỗ Trợ VIP 24/7</span>
                </span>
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            </button>

            <div class="flex items-center justify-between px-2 pt-2">
                <div class="flex items-center space-x-3">
                    <img src="https://placehold.co/100x100/3b82f6/ffffff?text=NV" alt="Avatar" class="w-9 h-9 rounded-full ring-2 ring-amber-500/40 object-cover">
                    <div>
                        <h4 class="text-sm font-semibold text-white">Nguyễn Văn An</h4>
                        <p class="text-[10px] text-amber-400 font-medium">VIP Diamond Member</p>
                    </div>
                </div>
                <button onclick="showNotification('Đã khóa phiên giao dịch an toàn.', 'info')" class="text-slate-400 hover:text-red-400 p-2 transition-colors" title="Đăng xuất">
                    <i class="fa-solid fa-power-off"></i>
                </button>
            </div>
        </div>
    </aside>

    <main class="flex-1 flex flex-col min-w-0 overflow-y-auto">
        
        <!-- Top Toolbar & Search Bar -->
        <header class="sticky top-0 z-40 bg-slate-900/80 backdrop-blur-md border-b border-slate-800 px-6 py-4 flex items-center justify-between">
            <div class="flex items-center space-x-4 flex-1 max-w-md">
                <div class="relative w-full">
                    <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none text-slate-400">
                        <i class="fa-solid fa-magnifying-glass text-sm"></i>
                    </span>
                    <input type="text" id="globalSearch" placeholder="Tìm kiếm dịch vụ, mã giao dịch, số tài khoản..." class="w-full pl-10 pr-4 py-2 bg-slate-800/80 border border-slate-700 rounded-xl text-sm text-slate-200 placeholder-slate-400 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-all">
                </div>
            </div>

            <div class="flex items-center space-x-3">
                <!-- Quick Service Filter Toggle -->
                <button onclick="showNotification('Đã áp dụng bộ lọc giao dịch thông minh.', 'info')" class="hidden sm:flex items-center space-x-2 px-3.5 py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-xl text-xs font-medium text-slate-300 transition-all">
                    <i class="fa-solid fa-filter text-amber-400"></i>
                    <span>Bộ Lọc Nhanh</span>
                </button>

                <!-- Notifications Button -->
                <div class="relative">
                    <button onclick="toggleNotifications()" class="w-10 h-10 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 flex items-center justify-center text-slate-300 hover:text-white transition-all relative">
                        <i class="fa-regular fa-bell"></i>
                        <span class="absolute top-2 right-2 w-2.5 h-2.5 bg-amber-500 rounded-full ring-2 ring-slate-900 animate-bounce"></span>
                    </button>
                    <!-- Notification Dropdown -->
                    <div id="notificationDropdown" class="hidden absolute right-0 mt-2 w-80 bg-slate-900 border border-slate-700 rounded-2xl shadow-2xl p-4 z-50">
                        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-3">
                            <h3 class="font-semibold text-sm text-white flex items-center space-x-2">
                                <i class="fa-solid fa-bell text-amber-400"></i>
                                <span>Thông Báo Gần Đây</span>
                            </h3>
                            <span class="text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-medium">2 chưa đọc</span>
                        </div>
                        <div class="space-y-2.5 max-h-64 overflow-y-auto pr-1">
                            <div class="p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 transition-all cursor-pointer">
                                <div class="flex items-start space-x-3">
                                    <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                                        <i class="fa-solid fa-arrow-down-long"></i>
                                    </div>
                                    <div>
                                        <p class="text-xs font-medium text-white">Nhận lương tháng 3/2026</p>
                                        <p class="text-[11px] text-slate-400">+25,000,000 VND từ Techcombank.</p>
                                        <span class="text-[10px] text-slate-500 mt-1 block">5 phút trước</span>
                                    </div>
                                </div>
                            </div>
                            <div class="p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 transition-all cursor-pointer">
                                <div class="flex items-start space-x-3">
                                    <div class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                                        <i class="fa-solid fa-shield-halved"></i>
                                    </div>
                                    <div>
                                        <p class="text-xs font-medium text-white">Bảo mật tài khoản</p>
                                        <p class="text-[11px] text-slate-400">Đã kích hoạt Smart OTP thành công.</p>
                                        <span class="text-[10px] text-slate-500 mt-1 block">1 giờ trước</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Currency & Region Badge -->
                <div class="hidden lg:flex items-center space-x-1.5 px-3 py-1.5 bg-slate-800/60 border border-slate-700/60 rounded-xl text-xs text-slate-300">
                    <i class="fa-solid fa-globe text-blue-400"></i>
                    <span>VN / VND</span>
                </div>
            </div>
        </header>

        <!-- Main Workspace Tabs -->
        <div class="p-6 md:p-8 space-y-8 max-w-7xl mx-auto w-full">

            <div id="tab-dashboard" class="space-y-8 tab-content">
                
                <!-- Balance & Summary Cards -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <!-- Main Balance Card -->
                    <div class="lg:col-span-2 rounded-3xl bg-gradient-to-r from-blue-950 via-blue-900 to-indigo-950 p-6 md:p-8 relative overflow-hidden shadow-2xl border border-blue-500/30">
                        <div class="absolute -right-10 -bottom-10 w-60 h-60 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
                        <div class="flex items-center justify-between mb-6">
                            <div>
                                <p class="text-xs md:text-sm text-blue-200 font-medium tracking-wide uppercase">Tài khoản thanh toán chính</p>
                                <p class="text-xs text-slate-300 font-mono mt-1">STK: 1903 8888 6688 99 • NexusPay</p>
                            </div>
                            <button onclick="toggleBalanceVisibility()" class="w-10 h-10 rounded-xl bg-white/10 hover:bg-white/20 flex items-center justify-center text-white backdrop-blur-md transition-all">
                                <i class="fa-regular fa-eye" id="eyeIcon"></i>
                            </button>
                        </div>
                        <div class="mb-6">
                            <h2 class="text-3xl md:text-4xl font-bold tracking-tight text-white" id="balanceDisplay">124,850,320 <span class="text-lg font-normal text-amber-400">VND</span></h2>
                        </div>
                        <div class="flex flex-wrap gap-3 pt-4 border-t border-white/10">
                            <button onclick="switchTab('transfer')" class="px-4 py-2.5 bg-amber-500 hover:bg-amber-400 text-slate-950 rounded-xl font-bold text-xs md:text-sm flex items-center space-x-2 shadow-lg transition-all">
                                <i class="fa-solid fa-paper-plane text-slate-950"></i>
                                <span>Chuyển Tiền Nhanh</span>
                            </button>
                            <button onclick="openTopupModal()" class="px-4 py-2.5 bg-blue-600/40 hover:bg-blue-600/60 text-white rounded-xl font-medium text-xs md:text-sm flex items-center space-x-2 backdrop-blur-md border border-white/20 transition-all">
                                <i class="fa-solid fa-plus text-amber-400"></i>
                                <span>Nạp Tiền Vào Ví</span>
                            </button>
                        </div>
                    </div>

                    <!-- Asset Growth Statistics Card -->
                    <div class="rounded-3xl glass-panel p-6 flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="font-semibold text-sm text-slate-200 flex items-center space-x-2">
                                    <i class="fa-solid fa-chart-line text-amber-400"></i>
                                    <span>Tài sản tích lũy</span>
                                </h3>
                                <span class="text-xs text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full font-medium">+14.2% năm</span>
                            </div>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between text-xs text-slate-400 mb-1">
                                        <span>Tiết kiệm trực tuyến</span>
                                        <span class="text-white font-medium">85,000,000 VND</span>
                                    </div>
                                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                                        <div class="bg-amber-500 h-full rounded-full" style="width: 70%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs text-slate-400 mb-1">
                                        <span>Quỹ đầu tư số</span>
                                        <span class="text-white font-medium">39,850,320 VND</span>
                                    </div>
                                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                                        <div class="bg-blue-500 h-full rounded-full" style="width: 30%;"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="pt-4 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
                            <span>Đã đồng bộ Real-time</span>
                            <button onclick="showNotification('Đã đồng bộ hóa danh mục tài sản.', 'success')" class="text-amber-400 hover:text-amber-300 font-medium">Làm mới</button>
                        </div>
                    </div>
                </div>

                <div>
                    <h3 class="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-4 flex items-center space-x-2">
                        <i class="fa-solid fa-bolt text-amber-400"></i>
                        <span>Dịch Vụ Tài Chính Nổi Bật</span>
                    </h3>
                    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-4">
                        <button onclick="switchTab('transfer')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-blue-600/20 text-blue-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-blue-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-right-left"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Chuyển Tiền</span>
                        </button>
                        <button onclick="openServiceModal('Thanh toán hóa đơn Điện/Nước')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-emerald-600/20 text-emerald-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-emerald-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-bolt"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Điện / Nước</span>
                        </button>
                        <button onclick="switchTab('savings')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-amber-600/20 text-amber-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-amber-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-piggy-bank"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Tiết Kiệm</span>
                        </button>
                        <button onclick="switchTab('cards')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-purple-600/20 text-purple-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-purple-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-credit-card"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Quản Lý Thẻ</span>
                        </button>
                        <button onclick="openServiceModal('Nạp tiền điện thoại & Data 5G')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-rose-600/20 text-rose-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-rose-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-mobile-screen"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Nạp 5G/Mobile</span>
                        </button>
                        <button onclick="openServiceModal('Đặt vé máy bay & Khách sạn 5 sao')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-cyan-600/20 text-cyan-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-cyan-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-plane-departure"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Vé Máy Bay</span>
                        </button>
                        <button onclick="openServiceModal('Đầu tư chứng khoán & Quỹ mở')" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-indigo-600/20 text-indigo-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-indigo-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-chart-pie"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Chứng Khoán</span>
                        </button>
                        <button onclick="openSupportModal()" class="p-4 rounded-2xl glass-panel hover:bg-slate-800/80 hover:border-amber-500/40 flex flex-col items-center text-center group transition-all">
                            <div class="w-12 h-12 rounded-xl bg-teal-600/20 text-teal-400 flex items-center justify-center text-lg mb-3 group-hover:scale-110 group-hover:bg-teal-600 group-hover:text-white transition-all shadow-md">
                                <i class="fa-solid fa-headset"></i>
                            </div>
                            <span class="text-xs font-medium text-slate-200">Trợ Giúp VIP</span>
                        </button>
                    </div>
                </div>

                <div class="rounded-3xl glass-panel p-6">
                    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
                        <div>
                            <h3 class="font-bold text-base text-white">Giao Dịch Gần Đây</h3>
                            <p class="text-xs text-slate-400">Danh sách biến động số dư cập nhật liên tục</p>
                        </div>
                        <div class="flex items-center space-x-2 w-full sm:w-auto">
                            <select id="filterType" onchange="filterTransactions()" class="bg-slate-800 border border-slate-700 text-xs rounded-xl px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-500">
                                <option value="all">Tất cả giao dịch</option>
                                <option value="in">Tiền vào (+)</option>
                                <option value="out">Tiền ra (-)</option>
                            </select>
                            <button onclick="switchTab('history')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-medium rounded-xl text-amber-400 transition-all">
                                Xem tất cả
                            </button>
                        </div>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse" id="transactionTable">
                            <thead>
                                <tr class="border-b border-slate-800 text-xs text-slate-400">
                                    <th class="py-3 px-4 font-medium">Giao dịch</th>
                                    <th class="py-3 px-4 font-medium">Mã GD / Nội dung</th>
                                    <th class="py-3 px-4 font-medium">Thời gian</th>
                                    <th class="py-3 px-4 font-medium text-right">Số tiền</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800/60 text-sm" id="transactionBody">
                                <tr class="hover:bg-slate-800/40 transition-colors" data-type="in">
                                    <td class="py-4 px-4 flex items-center space-x-3">
                                        <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0">
                                            <i class="fa-solid fa-arrow-down-long"></i>
                                        </div>
                                        <div>
                                            <p class="font-medium text-white">Nhận tiền từ CTY TNHH ABC</p>
                                            <p class="text-xs text-slate-400">Techcombank</p>
                                        </div>
                                    </td>
                                    <td class="py-4 px-4">
                                        <span class="text-xs font-mono text-slate-300">FT2603991823</span>
                                        <p class="text-xs text-slate-400">Luong thang 3/2026</p>
                                    </td>
                                    <td class="py-4 px-4 text-xs text-slate-400">Hôm nay, 08:30</td>
                                    <td class="py-4 px-4 text-right font-semibold text-emerald-400">+25,000,000 VND</td>
                                </tr>
                                <tr class="hover:bg-slate-800/40 transition-colors" data-type="out">
                                    <td class="py-4 px-4 flex items-center space-x-3">
                                        <div class="w-10 h-10 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center flex-shrink-0">
                                            <i class="fa-solid fa-arrow-up-long"></i>
                                        </div>
                                        <div>
                                            <p class="font-medium text-white">Chuyển tiền nhanh NAPAS</p>
                                            <p class="text-xs text-slate-400">TRAN VAN BINH</p>
                                        </div>
                                    </td>
                                    <td class="py-4 px-4">
                                        <span class="text-xs font-mono text-slate-300">FT2603881920</span>
                                        <p class="text-xs text-slate-400">Tra tien an trua</p>
                                    </td>
                                    <td class="py-4 px-4 text-xs text-slate-400">Hôm qua, 12:15</td>
                                    <td class="py-4 px-4 text-right font-semibold text-rose-400">-150,000 VND</td>
                                </tr>
                                <tr class="hover:bg-slate-800/40 transition-colors" data-type="out">
                                    <td class="py-4 px-4 flex items-center space-x-3">
                                        <div class="w-10 h-10 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center flex-shrink-0">
                                            <i class="fa-solid fa-bolt"></i>
                                        </div>
                                        <div>
                                            <p class="font-medium text-white">Thanh toán hóa đơn điện</p>
                                            <p class="text-xs text-slate-400">EVN HCMC</p>
                                        </div>
                                    </td>
                                    <td class="py-4 px-4">
                                        <span class="text-xs font-mono text-slate-300">FT2603771192</span>
                                        <p class="text-xs text-slate-400">KH: PE020019283</p>
                                    </td>
                                    <td class="py-4 px-4 text-xs text-slate-400">25/03/2026</td>
                                    <td class="py-4 px-4 text-right font-semibold text-rose-400">-850,000 VND</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <div id="tab-transfer" class="space-y-8 tab-content hidden">
                <div class="max-w-2xl mx-auto rounded-3xl glass-panel p-6 md:p-8">
                    <div class="flex items-center space-x-3 mb-6 pb-4 border-b border-slate-800">
                        <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-xl">
                            <i class="fa-solid fa-right-left"></i>
                        </div>
                        <div>
                            <h2 class="text-lg font-bold text-white">Chuyển Khoản & Thanh Toán Nhanh</h2>
                            <p class="text-xs text-slate-400">Chuyển tiền nội bộ, liên ngân hàng 24/7 hoặc quét mã QR</p>
                        </div>
                    </div>

                    <form onsubmit="handleTransfer(event)" class="space-y-5">
                        <div>
                            <label class="block text-xs font-medium text-slate-300 mb-2">Hình thức giao dịch</label>
                            <div class="grid grid-cols-3 gap-3">
                                <button type="button" class="p-3 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs flex flex-col items-center space-y-1 shadow-md">
                                    <i class="fa-solid fa-building-columns text-base"></i>
                                    <span>Nhanh 24/7</span>
                                </button>
                                <button type="button" class="p-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs flex flex-col items-center space-y-1 border border-slate-700">
                                    <i class="fa-solid fa-qrcode text-base"></i>
                                    <span>Mã QR Code</span>
                                </button>
                                <button type="button" class="p-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs flex flex-col items-center space-y-1 border border-slate-700">
                                    <i class="fa-solid fa-globe text-base"></i>
                                    <span>Quốc Tế</span>
                                </button>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1.5">Ngân hàng thụ hưởng</label>
                                <select class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-amber-500">
                                    <option>NexusBank (Nội bộ miễn phí)</option>
                                    <option>Vietcombank</option>
                                    <option>Techcombank</option>
                                    <option>MB Bank</option>
                                    <option>ACB</option>
                                    <option>TPBank</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1.5">Số tài khoản thụ hưởng</label>
                                <input type="text" required placeholder="Nhập số tài khoản" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-amber-500 font-mono">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-medium text-slate-300 mb-1.5">Số tiền chuyển (VND)</label>
                            <div class="relative">
                                <input type="number" required placeholder="0" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3.5 py-2.5 text-lg font-bold text-white placeholder-slate-500 focus:outline-none focus:border-amber-500">
                                <span class="absolute inset-y-0 right-0 flex items-center pr-4 text-sm font-semibold text-amber-400 pointer-events-none">VND</span>
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-medium text-slate-300 mb-1.5">Nội dung chuyển tiền</label>
                            <input type="text" placeholder="Nguyen Van An chuyen tien..." class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-amber-500">
                        </div>

                        <button type="submit" class="w-full py-3.5 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-bold rounded-xl shadow-lg shadow-amber-600/30 transition-all flex items-center justify-center space-x-2">
                            <i class="fa-solid fa-lock text-sm"></i>
                            <span>Xác Thực Smart OTP & Chuyển Tiền</span>
                        </button>
                    </form>
                </div>
            </div>

            <div id="tab-savings" class="space-y-8 tab-content hidden">
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <div class="lg:col-span-2 rounded-3xl glass-panel p-6 md:p-8">
                        <div class="flex items-center justify-between mb-6">
                            <div>
                                <h3 class="font-bold text-lg text-white">Sổ Tiết Kiệm Trực Tuyến</h3>
                                <p class="text-xs text-slate-400">Sinh lời an toàn với lãi suất VIP lên đến 7.8%/năm</p>
                            </div>
                            <button onclick="openCreateSavingsModal()" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-bold rounded-xl shadow-md transition-all">
                                <i class="fa-solid fa-plus mr-1"></i> Mở Sổ Mới
                            </button>
                        </div>

                        <div class="space-y-4">
                            <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700/80 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                                <div class="flex items-center space-x-4">
                                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-xl flex-shrink-0">
                                        <i class="fa-solid fa-piggy-bank"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-sm text-white">Tiết Kiệm Lãi Suất Linh Hoạt (6 Tháng)</h4>
                                        <p class="text-xs text-slate-400">STK: SV98231029 • Lãi suất: <span class="text-emerald-400 font-semibold">6.5%/năm</span></p>
                                    </div>
                                </div>
                                <div class="text-left sm:text-right">
                                    <p class="text-sm font-bold text-white">50,000,000 VND</p>
                                    <span class="text-[11px] text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-md font-medium">Đang sinh lời</span>
                                </div>
                            </div>

                            <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700/80 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                                <div class="flex items-center space-x-4">
                                    <div class="w-12 h-12 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-xl flex-shrink-0">
                                        <i class="fa-solid fa-shield-cat"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-sm text-white">Tiết Kiệm Tích Lũy Mục Tiêu Nhà Cửa</h4>
                                        <p class="text-xs text-slate-400">STK: SV98231991 • Lãi suất: <span class="text-emerald-400 font-semibold">7.2%/năm</span></p>
                                    </div>
                                </div>
                                <div class="text-left sm:text-right">
                                    <p class="text-sm font-bold text-white">35,000,000 VND</p>
                                    <span class="text-[11px] text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-md font-medium">Đang sinh lời</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Interest Calculator Widget -->
                    <div class="rounded-3xl glass-panel p-6 flex flex-col justify-between">
                        <div>
                            <h3 class="font-semibold text-sm text-white mb-2 flex items-center space-x-2">
                                <i class="fa-solid fa-calculator text-amber-400"></i>
                                <span>Tính Lãi Suất Online</span>
                            </h3>
                            <p class="text-xs text-slate-400 mb-4">Ước tính lợi nhuận tiền gửi tiết kiệm chính xác.</p>
                            
                            <div class="space-y-3">
                                <div>
                                    <label class="block text-[11px] text-slate-400 mb-1">Số tiền gửi (VND)</label>
                                    <input type="text" id="calcAmount" value="50000000" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white">
                                </div>
                                <div>
                                    <label class="block text-[11px] text-slate-400 mb-1">Kỳ hạn gửi</label>
                                    <select id="calcTerm" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white">
                                        <option value="6">6 tháng (6.5%)</option>
                                        <option value="12">12 tháng (7.5%)</option>
                                        <option value="24">24 tháng (7.8%)</option>
                                    </select>
                                </div>
                                <div class="p-3 rounded-xl bg-blue-950/60 border border-blue-500/30 mt-2">
                                    <p class="text-[11px] text-blue-300">Lãi dự tính nhận được:</p>
                                    <p class="text-base font-bold text-emerald-400" id="calcResult">3,250,000 VND</p>
                                </div>
                            </div>
                        </div>
                        <button onclick="calculateProfit()" class="w-full mt-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-amber-400 font-semibold text-xs rounded-xl border border-amber-500/30 transition-all">
                            Tính Ngay
                        </button>
                    </div>
                </div>
            </div>

            <div id="tab-cards" class="space-y-8 tab-content hidden">
                <div class="rounded-3xl glass-panel p-6 md:p-8">
                    <div class="flex items-center justify-between mb-6">
                        <div>
                            <h3 class="font-bold text-lg text-white">Quản Lý Thẻ & Bảo Mật Thanh Toán</h3>
                            <p class="text-xs text-slate-400">Khóa thẻ khẩn cấp, đổi mã PIN, quản lý hạn mức thanh toán quốc tế</p>
                        </div>
                        <button onclick="openOrderCardModal()" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-bold rounded-xl shadow-md transition-all">
                            <i class="fa-solid fa-plus mr-1"></i> Phát Hành Thẻ Mới
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        <!-- Visa Diamond Platinum Card -->
                        <div class="rounded-3xl bg-gradient-to-tr from-slate-900 via-blue-950 to-indigo-950 p-6 shadow-xl border border-amber-500/30 flex flex-col justify-between h-56 relative overflow-hidden group">
                            <div class="absolute right-4 top-4 text-amber-400">
                                <i class="fa-solid fa-crown text-xl"></i>
                            </div>
                            <div>
                                <p class="text-xs text-amber-300 font-semibold uppercase tracking-widest">Nexus Platinum Elite</p>
                                <p class="text-lg font-mono font-bold tracking-widest text-white mt-4">•••• •••• •••• 8829</p>
                            </div>
                            <div class="flex items-end justify-between">
                                <div>
                                    <p class="text-[10px] text-slate-400">Chủ thẻ</p>
                                    <p class="text-xs font-semibold text-white uppercase">NGUYEN VAN AN</p>
                                </div>
                                <div class="flex items-center space-x-2">
                                    <button onclick="toggleCardLock(this)" class="w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xs hover:bg-emerald-500 hover:text-white transition-all" title="Khóa/Mở khóa thẻ">
                                        <i class="fa-solid fa-lock-open"></i>
                                    </button>
                                    <i class="fa-brands fa-cc-visa text-3xl text-white"></i>
                                </div>
                            </div>
                        </div>

                        <!-- Mastercard Debit Card -->
                        <div class="rounded-3xl bg-gradient-to-tr from-slate-950 via-purple-950 to-slate-900 p-6 shadow-xl border border-purple-500/30 flex flex-col justify-between h-56 relative overflow-hidden group">
                            <div class="absolute right-4 top-4 text-purple-400">
                                <i class="fa-solid fa-shield-halved text-xl"></i>
                            </div>
                            <div>
                                <p class="text-xs text-purple-300 font-semibold uppercase tracking-widest">Nexus Debit Digital</p>
                                <p class="text-lg font-mono font-bold tracking-widest text-white mt-4">•••• •••• •••• 4410</p>
                            </div>
                            <div class="flex items-end justify-between">
                                <div>
                                    <p class="text-[10px] text-slate-400">Chủ thẻ</p>
                                    <p class="text-xs font-semibold text-white uppercase">NGUYEN VAN AN</p>
                                </div>
                                <div class="flex items-center space-x-2">
                                    <button onclick="toggleCardLock(this)" class="w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xs hover:bg-emerald-500 hover:text-white transition-all" title="Khóa/Mở khóa thẻ">
                                        <i class="fa-solid fa-lock-open"></i>
                                    </button>
                                    <i class="fa-brands fa-cc-mastercard text-3xl text-amber-500"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="tab-history" class="space-y-8 tab-content hidden">
                <div class="rounded-3xl glass-panel p-6 md:p-8">
                    <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 mb-6">
                        <div>
                            <h3 class="font-bold text-lg text-white">Lịch Sử Giao Dịch Toàn Bộ</h3>
                            <p class="text-xs text-slate-400">Tra cứu chi tiết mọi biến động số dư tài khoản ngân hàng</p>
                        </div>
                        <div class="flex items-center space-x-3 w-full md:w-auto">
                            <input type="date" class="bg-slate-800 border border-slate-700 text-xs rounded-xl px-3 py-2 text-slate-200 focus:outline-none">
                            <button onclick="showNotification('Đã xuất sao kê giao dịch thành công (PDF).', 'success')" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-bold rounded-xl shadow-md transition-all">
                                <i class="fa-solid fa-download mr-1"></i> Xuất Sao Kê
                            </button>
                        </div>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-800 text-xs text-slate-400">
                                    <th class="py-3 px-4 font-medium">Giao dịch</th>
                                    <th class="py-3 px-4 font-medium">Mã giao dịch</th>
                                    <th class="py-3 px-4 font-medium">Loại</th>
                                    <th class="py-3 px-4 font-medium">Thời gian</th>
                                    <th class="py-3 px-4 font-medium text-right">Số tiền</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800/60 text-sm">
                                <tr class="hover:bg-slate-800/40 transition-colors">
                                    <td class="py-4 px-4 flex items-center space-x-3">
                                        <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0">
                                            <i class="fa-solid fa-arrow-down text-xs"></i>
                                        </div>
                                        <div>
                                            <p class="font-medium text-white">Nhận tiền lương tháng 3</p>
                                            <p class="text-xs text-slate-400">Techcombank</p>
                                        </div>
                                    </td>
                                    <td class="py-4 px-4 font-mono text-xs text-slate-300">FT2603991823</td>
                                    <td class="py-4 px-4 text-xs text-emerald-400 font-medium">Tiền vào</td>
                                    <td class="py-4 px-4 text-xs text-slate-400">01/04/2026 08:30</td>
                                    <td class="py-4 px-4 text-right font-semibold text-emerald-400">+25,000,000 VND</td>
                                </tr>
                                <tr class="hover:bg-slate-800/40 transition-colors">
                                    <td class="py-4 px-4 flex items-center space-x-3">
                                        <div class="w-9 h-9 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center flex-shrink-0">
                                            <i class="fa-solid fa-arrow-up text-xs"></i>
                                        </div>
                                        <div>
                                            <p class="font-medium text-white">Thanh toán cước Internet VNPT</p>
                                            <p class="text-xs text-slate-400">VNPT Telecom</p>
                                        </div>
                                    </td>
                                    <td class="py-4 px-4 font-mono text-xs text-slate-300">FT2603981120</td>
                                    <td class="py-4 px-4 text-xs text-rose-400 font-medium">Tiền ra</td>
                                    <td class="py-4 px-4 text-xs text-slate-400">28/03/2026 14:20</td>
                                    <td class="py-4 px-4 text-right font-semibold text-rose-400">-320,000 VND</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

        </div>
    </main>

    <div id="toastContainer" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>

    <!-- Support / Chatbot Modal -->
    <div id="supportModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-md p-6 shadow-2xl relative">
            <button onclick="closeSupportModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
            <div class="flex items-center space-x-3 mb-4 pb-3 border-b border-slate-800">
                <div class="w-10 h-10 rounded-xl bg-amber-500 text-slate-950 flex items-center justify-center font-bold">
                    <i class="fa-solid fa-headset"></i>
                </div>
                <div>
                    <h3 class="font-bold text-white text-base">NexusCare VIP Support</h3>
                    <p class="text-xs text-slate-400">Trợ lý ngân hàng số trực tuyến 24/7</p>
                </div>
            </div>
            <div class="space-y-3 mb-4 max-h-60 overflow-y-auto pr-1 text-xs">
                <div class="p-3 rounded-2xl bg-slate-800 text-slate-200 max-w-[85%]">
                    Xin chào Nguyễn Văn An! Tổng đài NexusBank sẵn sàng hỗ trợ giao dịch của quý khách.
                </div>
            </div>
            <div class="flex items-center space-x-2">
                <input type="text" placeholder="Nhập câu hỏi của bạn..." class="flex-1 bg-slate-800 border border-slate-700 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-amber-500">
                <button onclick="showNotification('Đã gửi yêu cầu hỗ trợ đến chuyên viên.', 'success'); closeSupportModal();" class="px-4 py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs">Gửi</button>
            </div>
        </div>
    </div>

    <script>
        // Tab switching handler
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.getElementById('tab-' + tabId).classList.remove('hidden');

            document.querySelectorAll('aside nav a').forEach(el => {
                el.classList.remove('bg-blue-600', 'text-white', 'shadow-lg', 'shadow-blue-600/30');
                el.classList.add('text-slate-400');
            });
            const activeNav = document.getElementById('nav-' + tabId);
            if (activeNav) {
                activeNav.classList.remove('text-slate-400');
                activeNav.classList.add('bg-blue-600', 'text-white', 'shadow-lg', 'shadow-blue-600/30');
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Balance visibility toggle
        let isBalanceVisible = true;
        function toggleBalanceVisibility() {
            isBalanceVisible = !isBalanceVisible;
            const display = document.getElementById('balanceDisplay');
            const eye = document.getElementById('eyeIcon');
            if (isBalanceVisible) {
                display.innerHTML = '124,850,320 <span class="text-lg font-normal text-amber-400">VND</span>';
                eye.className = 'fa-regular fa-eye';
            } else {
                display.innerHTML = '•••••••••••• <span class="text-lg font-normal text-amber-400">VND</span>';
                eye.className = 'fa-regular fa-eye-slash';
            }
        }

        // Toast notifications
        function showNotification(message, type = 'success') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            const bgColor = type === 'success' ? 'bg-emerald-600' : 'bg-blue-600';
            toast.className = `${bgColor} text-white px-4 py-3 rounded-2xl shadow-2xl text-xs flex items-center space-x-2 transform translate-y-5 opacity-0 transition-all duration-300 pointer-events-auto`;
            toast.innerHTML = `<i class="fa-solid fa-circle-check text-sm"></i><span>${message}</span>`;
            container.appendChild(toast);

            setTimeout(() => {
                toast.classList.remove('translate-y-5', 'opacity-0');
            }, 10);

            setTimeout(() => {
                toast.classList.add('translate-y-5', 'opacity-0');
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        // Notification dropdown toggle
        function toggleNotifications() {
            const dropdown = document.getElementById('notificationDropdown');
            dropdown.classList.toggle('hidden');
        }

        // Support modal handlers
        function openSupportModal() {
            document.getElementById('supportModal').classList.remove('hidden');
        }
        function closeSupportModal() {
            document.getElementById('supportModal').classList.add('hidden');
        }

        // Quick service modals
        function openServiceModal(serviceName) {
            showNotification(`Đang mở cổng dịch vụ: ${serviceName}`, 'info');
        }
        function openTopupModal() {
            showNotification('Vui lòng chọn nguồn tiền nạp vào ví.', 'info');
            switchTab('transfer');
        }
        function openCreateSavingsModal() {
            showNotification('Mở sổ tiết kiệm trực tuyến thành công.', 'success');
        }
        function openOrderCardModal() {
            showNotification('Yêu cầu phát hành thẻ mới đã được ghi nhận.', 'success');
        }

        // Transfer submit
        function handleTransfer(event) {
            event.preventDefault();
            showNotification('Chuyển khoản thành công! Mã GD #FT26038891', 'success');
            event.target.reset();
        }

        // Card lock toggle
        function toggleCardLock(btn) {
            const icon = btn.querySelector('i');
            if (icon.classList.contains('fa-lock-open')) {
                icon.className = 'fa-solid fa-lock text-xs';
                btn.className = 'w-8 h-8 rounded-full bg-rose-500/20 text-rose-400 flex items-center justify-center text-xs hover:bg-rose-500 hover:text-white transition-all';
                showNotification('Đã khóa thẻ tạm thời để bảo mật.', 'info');
            } else {
                icon.className = 'fa-solid fa-lock-open text-xs';
                btn.className = 'w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xs hover:bg-emerald-500 hover:text-white transition-all';
                showNotification('Đã mở khóa thẻ thành công.', 'success');
            }
        }

        // Interest calculator
        function calculateProfit() {
            const amount = parseFloat(document.getElementById('calcAmount').value) || 0;
            const term = parseInt(document.getElementById('calcTerm').value);
            let rate = 0.065;
            if (term === 12) rate = 0.075;
            if (term === 24) rate = 0.078;
            const profit = (amount * rate * (term / 12));
            document.getElementById('calcResult').innerText = profit.toLocaleString('vi-VN') + ' VND';
        }

        // Transaction table filter
        function filterTransactions() {
            const type = document.getElementById('filterType').value;
            const rows = document.querySelectorAll('#transactionBody tr');
            rows.forEach(row => {
                const rowType = row.getAttribute('data-type');
                if (type === 'all' || rowType === type) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
