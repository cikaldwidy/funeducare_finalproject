document.addEventListener("DOMContentLoaded", function () {
  const childCards = document.querySelectorAll(".child-card");
  const developmentDetails = document.getElementById("development-details");
  const developmentList = document.getElementById("development-list");
  const developmentTitle = document.getElementById("development-title");

  // Function to get color based on development level
  function getTingkatColor(tingkat) {
    switch (tingkat) {
      case "Berkembang Sangat Baik":
        return "level-very-good";
      case "Berkembang Sesuai Harapan":
        return "level-expected";
      default:
        return "";
    }
  }

  // Function to get icon for development category
  function getCategoryIcon(kategori) {
    const icons = {
      "Sosial Emosional": "😊",
      Kognitif: "📖",
      Motorik: "🏃",
      Bahasa: "💬",
    };
    return icons[kategori] || "📝";
  }

  // Select child and show development details
  function selectChild(childCard) {
    // Reset previous selection
    childCards.forEach((card) => {
      card.classList.remove("selected");
    });

    // Highlight selected child
    childCard.classList.add("selected");

    // Get child ID
    const childId = childCard.dataset.childId;

    // Find development details for this child
    const developmentData = childDevelopmentsData.find(
      (child) => child.child.id == childId
    );

    if (developmentData) {
      // Update title
      developmentTitle.textContent = `Detail Perkembangan ${developmentData.child.name}`;

      // Clear previous details
      developmentList.innerHTML = "";

      // Render development items
      developmentData.developments.forEach((item) => {
        const developmentItem = document.createElement("div");
        developmentItem.className = "development-item";
        developmentItem.innerHTML = `
            <div class="development-icon">${getCategoryIcon(
              item.category
            )}</div>
            <div class="development-content">
              <div class="development-category">${item.category}</div>
              <div class="development-description">${item.description}</div>
              <span class="development-level ${getTingkatColor(item.level)}">${
          item.level
        }</span>
            </div>
          `;
        developmentList.appendChild(developmentItem);
      });

      // Show development details
      developmentDetails.style.display = "block";
    }
  }

  // Add click event to child cards
  childCards.forEach((card) => {
    card.addEventListener("click", () => selectChild(card));
  });

  // Automatically select first child if exists
  if (childCards.length > 0) {
    selectChild(childCards[0]);
  }
});
